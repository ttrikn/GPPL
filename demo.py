import sys
from PIL import Image
import requests
import torch
from torchvision import transforms
from torchvision.transforms.functional import InterpolationMode
from models.blip import blip_feature_extractor
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def load_demo_images(image_size, device, num_images=34):
    images = []

    for i in range(1, num_images + 1):
        img_url = f"D://PyCharm/FS1/UP-MPF-main/datasets/TWITTER/{i}.jpg"
        raw_image = Image.open(img_url).convert('RGB')
        raw_image = raw_image.resize((raw_image.width // 5, raw_image.height // 5))  # 在原地调整大小

        transform = transforms.Compose([
            transforms.Resize((image_size, image_size), interpolation=InterpolationMode.BICUBIC),
            transforms.ToTensor(),
            transforms.Normalize((0.48145466, 0.4578275, 0.40821073), (0.26862954, 0.26130258, 0.27577711))
        ])

        image = transform(raw_image).unsqueeze(0)
        images.append(image)

    images = torch.cat(images, dim=0).to(device)
    return images

image_size = 224
num_images = 34
images = load_demo_images(image_size=image_size, device=device, num_images=num_images)

model_url = 'D://PyCharm/FS1/model_base_capfilt_large.pth'
print(images.shape)

model = blip_feature_extractor(pretrained=model_url, image_size=image_size, vit='base')
model.eval()
model = model.to(device)


image_features = model(images, '', mode='image')[:, 0].unsqueeze(1)
print(image_features.shape)

