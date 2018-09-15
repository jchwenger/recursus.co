import os
import glob
from PIL import Image

files = glob.glob('*.jpg')

for fl in files:
    img = Image.open(fl)
    if img.size[0] > img.size[1]:
        os.rename(fl, fl[:-4]+'_horiz.jpg')
    else:
        os.rename(fl, fl[:-4]+'_vert.jpg')
