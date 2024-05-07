import torch.nn as nn
import torch
import torch.nn.functional as F
from backbone import CBAM
import math
import os
import math
from .feature_pyramid_network   import *
from torchvision.ops.misc import FrozenBatchNorm2d
try:
    from torch.hub import load_state_dict_from_url
except ImportError:
    from torch.utils.model_zoo import load_url as load_state_dict_from_url

model_urls = {
    'resnet18': 'https://download.pytorch.org/models/resnet18-5c106cde.pth',
    'resnet34': 'https://download.pytorch.org/models/resnet34-333f7ec4.pth',
    'resnet50': 'https://download.pytorch.org/models/resnet50-19c8e357.pth',
    'resnet101': 'https://download.pytorch.org/models/resnet101-5d3b4d8f.pth',
    'resnet152': 'https://download.pytorch.org/models/resnet152-b121ed2d.pth',
    'resnext50_32x4d': 'https://download.pytorch.org/models/resnext50_32x4d-7cdf4587.pth',
    'resnext101_32x8d': 'https://download.pytorch.org/models/resnext101_32x8d-8ba56ff5.pth',
}
'''
    Resnet 残差块
'''
class Bottleneck(nn.Module):
    expansion = 4

    def __init__(self, in_channel, out_channel, stride=1, downsample=None, norm_layer=None):
        super().__init__()
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d

        self.conv1 = nn.Conv2d(in_channels=in_channel, out_channels=out_channel,
                               kernel_size=1, stride=1, bias=False)  # squeeze channels
        self.bn1 = norm_layer(out_channel)
        # -----------------------------------------
        self.conv2 = nn.Conv2d(in_channels=out_channel, out_channels=out_channel,
                               kernel_size=3, stride=stride, bias=False, padding=1)
        self.bn2 = norm_layer(out_channel)
        # -----------------------------------------
        self.conv3 = nn.Conv2d(in_channels=out_channel, out_channels=out_channel * self.expansion,
                               kernel_size=1, stride=1, bias=False)  # unsqueeze channels
        self.bn3 = norm_layer(out_channel * self.expansion)
        self.relu = nn.ReLU(inplace=True)
        self.downsample = downsample


    def forward(self, x):
        residual = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu(out)

        out = self.conv3(out)
        out = self.bn3(out)

        # out = self.ca(out) * out
        # out = self.sa(out) * out
        if self.downsample is not None:
            residual = self.downsample(x)
        out += residual
        out = self.relu(out)
        return out


class ResNet_CBAM(nn.Module):
    def __init__(self, block, layers, num_classes=1000
                 , include_top=True, norm_layer=None):
        super(ResNet_CBAM, self).__init__()
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        self._norm_layer = norm_layer
        self.include_top = include_top
        self.in_channel = 64
        self.conv1 = nn.Conv2d(3, self.in_channel, kernel_size=7,
                               stride=2, padding=3,
                               bias=False)
        self.bn1 = self._norm_layer(self.in_channel)
        self.relu = nn.ReLU(inplace=True)

        # 网络的第一层加入注意力机制
        self.ca = CBAM.ChannelAttention(self.in_channel)
        self.sa = CBAM.SpatialAttention()

        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        self.layer1 = self._make_layer(block, 64, layers[0])
        self.layer2 = self._make_layer(block, 128, layers[1], stride=2)
        self.layer3 = self._make_layer(block, 256, layers[2], stride=2)
        self.layer4 = self._make_layer(block, 512, layers[3], stride=2)
        # 网络的卷积层的最后一层加入注意力机制
        self.ca1 = CBAM.ChannelAttention(self.in_channel)
        self.sa1 = CBAM.SpatialAttention()
        if self.include_top:
            # self.avgpool=nn.AvgPool2d(7)
            self.avgpool = nn.AdaptiveAvgPool2d((1, 1))  # output size = (1, 1)
            self.fc = nn.Linear(512 * block.expansion, num_classes)
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2. / n))
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()

    def _make_layer(self, block, channel, blocks, stride=1):
        downsample = None
        if stride != 1 or self.in_channel != channel * block.expansion:
            downsample = nn.Sequential(
                nn.Conv2d(self.in_channel, channel * block.expansion,
                          kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(channel * block.expansion))
        layers = []
        layers.append(block(self.in_channel, channel, stride, downsample))
        self.in_channel = channel * block.expansion
        for i in range(1, blocks):
            layers.append(block(self.in_channel, channel))
        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)

        x = self.ca(x) * x
        x = self.sa(x) * x

        x = self.maxpool(x)

        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        x = self.ca1(x) * x
        x = self.sa1(x) * x

        x = self.avgpool(x)
        x = x.reshape(x.size(0), -1)
        x = self.fc(x)
        return x

def _resnet(arch, pretrained, progress, **kwargs):
    model = ResNet_CBAM(Bottleneck, [3, 4, 6, 3], **kwargs)
    if pretrained:
        pretrained_state_dict = load_state_dict_from_url(model_urls[arch])
        model_dict = model.state_dict()
        pretrained_dict = {k: v for k, v in pretrained_state_dict.items() if k in model_dict}
        model_dict.update(pretrained_dict)
        model.load_state_dict(model_dict)
        # pretrained_dict = torch.load(kwargs['model_path'])['state_dict']  # torch.load得到是字典，我们需要的是state_dict下的参数
    return model
def resnet50_cbam(pretrained=True, progress=True,
                  norm_layer=FrozenBatchNorm2d,
                  trainable_layers=5,
                  **kwargs):
    """Constructs a ResNet-50 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
        progress (bool): If True, displays a progress bar of the download to stderr
    """
    resnet_backbone=_resnet('resnet50', pretrained, progress,**kwargs)
    if isinstance(norm_layer, FrozenBatchNorm2d):
        overwrite_eps(resnet_backbone, 0.0)

    assert 0 <= trainable_layers <= 5
    layers_to_train = ['layer4', 'layer3', 'layer2', 'layer1', 'conv1'][:trainable_layers]
    # 如果要训练所有层结构的话，不要忘了conv1后还有一个bn1
    if trainable_layers == 5:
        layers_to_train.append("bn1")
        # layers_to_train.append("fc")
    # freeze layers
    for name, parameter in resnet_backbone.named_parameters():
        # 只训练不在layers_to_train列表中的层结构
        if all([not name.startswith(layer) for layer in layers_to_train]):
            parameter.requires_grad_(False)
    return resnet_backbone
def overwrite_eps(model, eps):
    """
    This method overwrites the default eps values of all the
    FrozenBatchNorm2d layers of the model with the provided value.
    This is necessary to address the BC-breaking change introduced
    by the bug-fix at pytorch/vision#2933. The overwrite is applied
    only when the pretrained weights are loaded to maintain compatibility
    with previous versions.

    Args:
        model (nn.Module): The model on which we perform the overwrite.
        eps (float): The new value of eps.
    """
    for module in model.modules():
        if isinstance(module, FrozenBatchNorm2d):
            module.eps = eps

def resnet50_fpn_backbone(pretrained=True,
                          returned_layers=None,
                          extra_blocks=None):
    """Constructs a ResNet-50 model.
    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
        progress (bool): If True, displays a progress bar of the download to stderr
    """
    from torchvision.models.feature_extraction import create_feature_extractor
    resnet_backbone=resnet50_cbam(pretrained)
    in_channels_list = [256, 512, 1024, 2048]
        # freeze layers
    if extra_blocks is None:
        extra_blocks = LastLevelMaxPool()
    returned_layers = {'layer1': '0', 'layer2': '1', 'layer3': '2', 'layer4': '3'}
    resnet_backbone = create_feature_extractor(resnet_backbone, returned_layers)
    backbone_with_fpn = BackboneWithFPN(resnet_backbone,
                                        return_layers=returned_layers,
                                        in_channels_list=in_channels_list,
                                        out_channels=256,
                                        extra_blocks=extra_blocks,
                                        re_getter=False)
    return backbone_with_fpn