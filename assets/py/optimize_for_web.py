import os
import glob
from PIL import Image

files = glob.glob('*.jpg')


for fl in files:
    img = Image.open(fl)

    # for horizontal pics
    if img.size[0] > img.size[1]:
        
        hor_width = 1000
        hor_height = int(hor_width * img.size[1] / img.size[0])
        img = img.resize((hor_width, hor_height), Image.ANTIALIAS)
        img.save(fl)

    # for vertical pics
    else:
        vert_height = 1000
        vert_width = int(vert_height * img.size[0] / img.size[1])
        img = img.resize((vert_width, vert_height), Image.ANTIALIAS)
        img.save(fl)

