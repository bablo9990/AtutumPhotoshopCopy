import os

from PIL import ImageFilter
from PIL import Image

image = Image.open("D:/Рабочий стол/knife.png")
Blur = image.filter(ImageFilter.BLUR)
if not (os.path.exists('D:/Рабочий стол/ModifiedImage/') and os.path.isdir('D:/Рабочий стол/ModifiedImage/')):
    print('Exiting...')
    os.mkdir('D:/Рабочий стол/ModifiedImage/')
Blur.save('D:/Рабочий стол/ModifiedImage/blur.png')