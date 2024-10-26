from flask import Flask, request, jsonify, render_template
from PIL import Image
import timm
import torch
import numpy as np
from torchvision import transforms
from skimage.metrics import structural_similarity as ssim
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,  # 根据访问者的IP记录访问次数
    default_limits=["20 per minute"]  # 默认限制，一分钟最多访问20次
)

# Load model
model = timm.create_model('resnet18', checkpoint_path="ckpt/pytorch_model.bin")
model.eval()

# 读取原图和设置原始标签
ori_path = "figure/cat.png"
ori_img = Image.open(ori_path).convert('RGB')
ori_img_numpy = np.array(ori_img)
ori_label = 282

# 定义data aug
data_transforms = transforms.Compose([
       transforms.ToTensor(),
       transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/CTF_home')
def home():
    return render_template('index.html')

@app.route('/CTF_games_upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded.'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file.'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed.'}), 400

    try:
        # Read the image directly from the uploaded file
        img = Image.open(file.stream)  # Use file.stream to read directly
        img.verify()  # Verify the image is valid
        img = Image.open(file.stream).convert('RGB')  # Reopen the image after verification
        img_numpy = np.array(img)
    except Exception as e:
        return jsonify({'error': 'Invalid image file.'}), 400

    if np.array(ori_img).shape != np.array(img).shape:
        return jsonify({
            '原始图像的尺寸为': np.array(ori_img).shape,
            'msg': "大小都和原图不一样, 这都想骗我？传张原图看看规则吧"
        })
    
    def compute_patch_ssim(ori_img, img, patch_size=(28, 28)):
        h, w, _ = ori_img.shape
        ssim_values = []

        for i in range(0, h, patch_size[0]):
            for j in range(0, w, patch_size[1]):
                ori_patch = ori_img[i:i+patch_size[0], j:j+patch_size[1]]
                img_patch = img[i:i+patch_size[0], j:j+patch_size[1]]
                
                # 确保patch大小一致
                if ori_patch.shape == img_patch.shape:
                    ssim_value = ssim(ori_patch / 255.0, img_patch / 255.0, multichannel=True, channel_axis=2)
                    ssim_values.append(ssim_value * 100)

        return ssim_values
    
    s = compute_patch_ssim(ori_img_numpy, img_numpy)
    
    s_Threshold = 90
    has_value_less_than_s_Threshold = any(value < s_Threshold for value in s)
    
    if has_value_less_than_s_Threshold:
        return jsonify({
            '原始类别(任务目标1: 目标类别≠预测类别)': ori_label,
            '预测类别': '传张像点的嘛~, 你这样不给你预测了',
            f'SSIM(任务目标2: 图片被切割成64块28×28的切块, 并对每个切块计算SSIM, 要求每个切块原图与扰动图的SSIM >= {s_Threshold})': s,
        })
    
    # Process the image for prediction
    output = model(data_transforms(img).unsqueeze(0))  # Unsqueeze single image into batch of 1

    top5_probabilities, top5_class_indices = torch.topk(output.softmax(dim=1), k=5)

    if top5_class_indices.squeeze().tolist()[0] == ori_label:
        return jsonify({
            '原始类别(任务目标1: 目标类别≠预测类别)': ori_label,
            '预测类别': top5_class_indices.squeeze().tolist()[0],
            f'SSIM(任务目标2: 图片被切割成64块28×28的切块, 并对每个切块计算SSIM, 要求每个切块原图与扰动图的SSIM >= {s_Threshold})': s,
            '预测概率': top5_probabilities.squeeze().tolist()[0],
        })
    else:
        return jsonify({
            '原始类别(任务目标1: 目标类别≠预测类别)': ori_label,
            '预测类别': top5_class_indices.squeeze().tolist()[0],
            f'SSIM(任务目标2: 图片被切割成64块28×28的切块, 并对每个切块计算SSIM, 要求每个切块原图与扰动图的SSIM >= {s_Threshold})': s,
            'msg': "牛的, 给你flag: XSCTF{You_R_New_NEW_Give_U_F1Ag_aNd_M1lkTea}, 记得保存攻击成功的图片~",
            '预测概率': top5_probabilities.squeeze().tolist()[0],
        })

if __name__ == '__main__':
    app.run(host ='0.0.0.0',port=9999)