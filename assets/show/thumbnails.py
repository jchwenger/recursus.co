# https://stackoverflow.com/questions/8631076/what-is-the-fastest-way-to-generate-image-thumbnails-in-python#8631924
from PIL import Image
import glob

sizes = [(120,120)]
files = glob.glob('*.jpg')

for image in files:
    for size in sizes:
        img = Image.open(image)
        img.thumbnail(size, Image.ANTIALIAS)
        img.save("{}_{}_thumbnail".format(image[:-4], '_'.join(map(str, size))) + '.jpg')
