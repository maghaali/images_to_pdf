#!/usr/bin/env python3
from PIL import Image
import os
import sys

image_folder_path = sys.argv[1]

images_list = []
list_dir = os.listdir(image_folder_path)

for image in list_dir:
    images_list.append(Image.open(image_folder_path+f"/{image}"))

images_list[0].save(image_folder_path+'/images.pdf',save_all=True, append_images=images_list[1:])
