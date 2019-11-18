from PIL import Image
import os

def rescale_images(directory, size):
    for img in os.listdir(directory):
        im = Image.open(directory+img)
        im_resized = im.resize(size, Image.ANTIALIAS)
        im_resized.save(directory+img)

directory = "../object_detection/dataset/flowers-recognition/flowers/sunflower"
size = (800,600)
for img in os.listdir(directory):
    im = Image.open(directory + "/" + img)
    im_resized = im.resize(size,Image.ANTIALIAS)
    im_resized.save(directory + "/" + img)
