# -*- coding: utf-8 -*-
"""
Code that allows to crop images in 1280 × 1024 and to group them in a same repertory.

"""

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import glob
import cv2
import pathlib
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--im_dir', type=str, help='Repertory that contains all the images of all the experiments', required=True)

args = parser.parse_args()

IM_DIR = args.im_dir

RESULT_DIR = pathlib.PurePath(IM_DIR).with_name(pathlib.PurePath(IM_DIR).name + '_crop')

# Input image extensions
IN_EXT = '.bmp'
# Output image extensions
OUT_EXT = '.png'

X_crop = 1280
Y_crop = 1024

SEP = '+'

# We remove the results repertory if it already exists
shutil.rmtree(RESULT_DIR, ignore_errors = True)

# Creation of the directory containing the results
try:
    os.makedirs(RESULT_DIR)
except OSError:
    pass

img_list_name = glob.glob(os.path.join(IM_DIR, '**/*' + IN_EXT), recursive=True)

for img_name in img_list_name:
    
    img = cv2.imread(img_name,cv2.IMREAD_GRAYSCALE)
    img_crop = img[int(img.shape[0]/2)-int(Y_crop/2):int(img.shape[0]/2)+int(Y_crop/2),int((img.shape[1])/2)-int(X_crop/2):int((img.shape[1])/2)+int(X_crop/2)]
    
    crop_name = pathlib.PurePath(img_name).with_suffix(OUT_EXT)
    crop_name = crop_name.relative_to(pathlib.PurePath(IM_DIR))
    crop_name = str(pathlib.PurePath(crop_name)).replace(os.sep, SEP)

    cv2.imwrite(os.path.join(RESULT_DIR, crop_name), img_crop)