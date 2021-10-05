# This is to be a simple project that will organize all given images in a folder

import os
import sys

from PIL import Image
from PIL.ExifTags import TAGS
from pprint import pprint

def get_images(path):
    images = []
    for f in os.listdir():
        if f.split('.').pop() in ['png', 'jpg', 'jpeg']:
            print('IMAGE FOUND: ' + f)
            work_image(f)


def work_image(img):
  i = Image.open(img)
  info = i._getexif()
  return {TAGS.get(tag): value for tag, value in info}

if __name__ == '__main__':
    get_images(sys.argv[0])
