* **题目名称：** 坏掉了的图片

* **题目类型：** MISC

* **题目难度：** (简单)

* **出题人：** HvAng

* **考点：**  

1. jpg图片高修改
2. steghide

* **描述：**  

* **flag：** XSCTF{Do_yOu_w@nt_t0_Go_Fi5h_fri3d_With_Klee?}

* **Writeup：**

压缩包注释或文件尾解Base64得到图片的高度为1231即0x4CF，找FF C0 00 11 08，它之后的两个字节为jpg图片的高，再后两格字节为宽。然后得到完整的jpg图片，可以看到图片里面有字符串，Dod0co，这是一个密钥，考虑隐写，即steghide，安装工具，steghide extract -sf Klee.jpg -p Dod0co，得到flag.txt。注意，解密需要图片为原来的高度
