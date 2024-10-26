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
    key_func=get_remote_address,   # 根据访问者的IP记录访问次数
    default_limits=["20 per minute"]  # 默认限制，一分钟最多访问20次
)

# Load model
model = timm.create_model('resnet18', checkpoint_path="ckpt/pytorch_model.bin")
model.eval()
ori_path = "figure/cat.png"
ori_img = Image.open(ori_path).convert('RGB')
ori_label = 282

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
    except Exception as e:
        return jsonify({'error': 'Invalid image file.'}), 400

    if np.array(ori_img).shape != np.array(img).shape:
        return jsonify({
            '图像尺寸为': np.array(ori_img).shape,
            'msg': "大小都和原图不一样, 不要欺骗我了555, 传张原图看看规则吧"
        })
    
    s = ssim(np.array(ori_img), np.array(img), multichannel=True, channel_axis=2)
    s *= 100. # 0~100, 越高越相似
    mse = float(np.mean( (np.array(ori_img).astype('float32') - np.array(img).astype('float32')) ** 2 ))
    
    if s < 90 or mse > 1000:
        return jsonify({
            '原始类别（任务目标1：目标类别≠预测类别）': ori_label,
            '预测类别': '传张像点的嘛~, 你这样不给你预测了',
            'ssim（任务目标2：SSIM>=90）': s,
            'mse（任务目标3：mse<=1000）': mse,
        })
    
    # Process the image for prediction
    output = model(data_transforms(img).unsqueeze(0))  # Unsqueeze single image into batch of 1

    top5_probabilities, top5_class_indices = torch.topk(output.softmax(dim=1), k=5)

    if top5_class_indices.squeeze().tolist()[0] == ori_label:
        return jsonify({
            '原始类别（任务目标1：目标类别≠预测类别）': ori_label,
            '预测类别': top5_class_indices.squeeze().tolist()[0],
            'ssim（任务目标2：SSIM>=90）': s,
            'mse（任务目标3：mse<=1000）': mse,
        })
    else:
        return jsonify({
            '原始类别（任务目标1：目标类别≠预测类别）': ori_label,
            '预测类别': top5_class_indices.squeeze().tolist()[0],
            'ssim（任务目标2：SSIM>=90）': s,
            'msg': "牛的，给你flag：XSCTF{You_R_New_NEW_Give_U_F1Ag_aNd_M1lkTea}",
            'mse（任务目标3：mse<=1000）': mse,
        })

if __name__ == '__main__':
    app.run(host ='0.0.0.0',port=9999)