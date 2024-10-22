import string
from secret import flag


# ぬん！
def s_hi_ka(text):
    offset = 1
    enc = ''
    for w in text:
        if w in string.ascii_letters:
            enc += chr(ord(w) + offset)
        else:
            enc += w
        offset *= -1
    return enc


# しかのこのこのここしたんたん
# 凯撒子恬不知耻地凯视眈眈
# しかのこのこのここしたんたん
# 凯撒子若无其事地凯视眈眈
# しかのこのこのここしたんたん
# 凯撒子寡廉鲜耻地凯视眈眈
# しかのこのこのここしたんたん!
# 凯撒子厚颜无耻地凯视眈眈!
# (一阵强劲的音乐)
with open("shikaed_flag.txt", "w+") as shika:
    shika.write(s_hi_ka(flag))
