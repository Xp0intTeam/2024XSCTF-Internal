* **题目名称：** CTF-简单对抗攻击

* **题目类型：** MISC

* **题目难度：** 中等

* **出题人：** gbljdgb

* **考点：**  AI图像对抗攻击

* **描述：**  
题目附件下载链接: https://pan.baidu.com/s/16BLmFg54EY2YQi2bPmFQNA 提取码: tha5  
对在ImageNet数据集上预训练的resnet18模型进行对抗攻击，通过给图像添加扰动让分类模型预测错误，同时尽可能保持图片的视觉不变性  
关于题目更加详细的描述见附件内README.md

* **flag：** XSCTF{You_R_New_NEW_Give_U_F1Ag_aNd_M1lkTea}

* **Writeup：**
运行payload.py生成扰动后的图片，上传即可获得flag
```python
python payload.py
```
