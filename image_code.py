#!/usr/bin/python3


from PIL import Image as img
import PIL

image1 = img.open("photo1.jpg")
print(image1.size, image1.format, image1.mode)
refait = image1.resize((1487,897))
print(refait.size)
refait.save("photo1.png")
