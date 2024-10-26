import torchattacks
from PIL import Image
import timm
import torch
from utils import imshow, get_pred
import cv2, os
import numpy as np
from torchvision import transforms

# Set the deterministic mode
torch.backends.cudnn.deterministic = True

# Load the model
model = timm.create_model('resnet18', checkpoint_path="ckpt/pytorch_model.bin")
model = model.eval()

# Load your images
images = []  # Placeholder for image tensor list
labels = []  # Placeholder for corresponding labels

data_transforms = transforms.Compose([
       transforms.ToTensor(),
       transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# 开始攻击
image_paths = ['figure/cat.png', 'figure/cat.png']  # Example paths
for img_path in image_paths:
    img = Image.open(img_path).convert('RGB')  # Load image
    img = data_transforms(img)  # Preprocess image
    images.append(img)
images = torch.stack(images)  # Convert list of tensors to a single tensor

labels = torch.tensor([282, 282])  # 根据你的实际情况修改

# Generate adversarial examples
atk = torchattacks.PGD(model, eps=8/255, alpha=2/255, steps=4, random_start=True)
atk.set_normalization_used(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
print(atk)

adv_images = atk(images, labels)

idx = 0
pre = get_pred(model, adv_images[idx:idx+1], device='cpu')
adv_img = imshow(adv_images[idx:idx+1], title="True:%d, Pre:%d"%(labels[idx], pre))
adv_img = cv2.cvtColor((adv_img*255).astype(np.uint8), cv2.COLOR_RGB2BGR)
cv2.imwrite(os.path.join('figure', 'NO.png'), adv_img)