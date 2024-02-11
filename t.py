import numpy as np
from PIL import Image

# 读取图片文件，转换为灰度模式
im = Image.open("t.png").convert("L")

# 将图片转换为numpy数组
img = np.array(im)

# 设置阈值，将数组中大于阈值的元素设为255（白色），小于等于阈值的元素设为0（黑色）
threshold = 128
img[img > threshold] = 255
img[img <= threshold] = 0

# 将数组转换回图片
im = Image.fromarray(img)

# 保存图片到文件
im.save("test_bin.jpg")
