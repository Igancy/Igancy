from PIL import Image
from os import listdir
from os.path import isfile, join
import time

mypath = input('Enter the file path Example:"F:\Minecraft\Content\Marketing Art\ ')
imagelist = [file for file in listdir(mypath) if file.endswith('.png')]
images = []

for j in range(len(imagelist)):
    x = imagelist[j]
    images.append(x.replace('.png', ''))
    j+1

for i in range(len(imagelist)):
    im1 = Image.open(mypath + imagelist[i])
    im1 = im1.convert("RGB")
    im1 = im1.resize((800,450))
    im1.save(mypath + images[i]+'.jpg')
    print("Image " + str(i+1) + " Converted")
    i+1
    time.sleep(.5)
print("Finished")
