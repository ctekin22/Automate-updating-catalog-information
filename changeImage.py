#!/usr/bin/env python3
""" In this section, you will write a Python script named changeImage.py to process the supplier images. 
You will be using the PIL library to update all images within ~/supplier-data/images directory."""

from PIL import Image
from os import listdir
import os
import glob

# Size: Change image resolution from 3000x2000 to 600x400 pixel
# Format: Change image format from .TIFF to .JPEG

img_dir ="./supplier-data/images"

for image in glob.glob(os.path.join(img_dir, "*.tiff")):
    image_name, ext = os.path.splitext(image)
    im=Image.open(image)
    im= im.resize((600,400))
    if im.mode != 'RGB':
        im = im.convert('RGB')
    image_name_splitted=image_name.split("/")[-1]
#    print(img_dir+ "/" +image_name_splitted + ".jpeg")
    im.save(os.path.join(img_dir,image_name_splitted) + ".jpeg", "JPEG")
