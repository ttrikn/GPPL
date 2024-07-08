import timm
import torch
import torch.nn as nn
from transformers import BertTokenizer, BertForMaskedLM
from torchvision import transforms
from PIL import Image
from param import args


ckpt_dict = torch.load(args.up_model_path, map_location='cpu')
for i in ckpt_dict["embedding"]:
    print(i)

print(len(ckpt_dict))
#
# ckpt_dict2 = torch.load("D://PyCharm/FS1/ImageNet_RotNet_AlexNet/model_net_epoch50.bin", map_location='cpu')
# for i in ckpt_dict2:
#     print(i)
#
# print(ckpt_dict2["epoch"])


class VisualEncoder(nn.Module):
    def __init__(self, model_name, pooling_scale, embedding_dim):
        '''for ResNet only'''
        super().__init__()
        self.backbone = timm.create_model(model_name, pretrained=True)

        x = int(pooling_scale[0])
        y = int(pooling_scale[1])
        print(f'[#] Image Tokens: (49, 2048) -> ({x}×{y}, {embedding_dim})')

        self.local_pool = nn.Sequential(
            nn.AdaptiveAvgPool2d((x, y)),  # (bs, 2048, 7, 7) -> (bs, 2048, x, y)
            nn.Flatten(2, -1)  # -> (bs, 2048, xy)
        )
        self.visual_mlp = nn.Linear(2048, embedding_dim, bias=False)

    def forward(self, imgs_tensor):
        visual_embeds = self.backbone.forward_features(imgs_tensor)  # (bs, 3, 224, 224) -> (bs, 2048, 7, 7)
        visual_embeds = self.local_pool(visual_embeds)  # (bs, 2048, xy)
        visual_embeds = visual_embeds.permute(0, 2, 1)  # (bs, xy, 2048)
        visual_embeds = self.visual_mlp(visual_embeds)  # (bs, xy, 768)

        return visual_embeds


image_path = "D://PyCharm/FS1/UP-MPF-main/datasets/MVSA-S_data/1.jpg"
img = Image.open(image_path).convert("RGB")
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

img_tensor = preprocess(img).unsqueeze(0)  # 添加批次维度
print(img_tensor.shape)

# 创建并运行模型
visual_encoder = VisualEncoder('nf_resnet50', '11', 768)
#visual_encoder.load_state_dict(ckpt_dict["embedding"])
visual_embeds = visual_encoder(img_tensor)
#print(visual_embeds)
print(visual_embeds.shape)

