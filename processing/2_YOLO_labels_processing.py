# -*- coding: utf-8 -*-
"""
Code that takes as input the txt files returned by YOLO contained in a single 
directory and returns text files containing
the particle's diameter in pixels.

(1.0, 1.0) becomes (1024, 1280)

"""

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import glob
import pathlib
import argparse
import shutil
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--label_dir', type=str, help='Repertory that contains all the labels of all the images', required=True)

args = parser.parse_args()

LABEL_DIR = args.label_dir
RESULT_DIR = pathlib.PurePath(args.label_dir).with_name(pathlib.PurePath(args.label_dir).name + "_results")

X_image = 1280
Y_image = 1024

SEP = '+'

# We remove the results repertory if it already exists
shutil.rmtree(RESULT_DIR, ignore_errors = True)

try:
    os.makedirs(RESULT_DIR)
except OSError:
    pass
    
txt_list_name = glob.glob(os.path.join(LABEL_DIR, '*.txt'))

for txt_name in tqdm(txt_list_name):
    f_name = pathlib.PurePath(str(pathlib.PureWindowsPath(txt_name).name).replace(SEP, os.sep))
    
    try:
       os.makedirs(os.path.join(RESULT_DIR, f_name.parent.parent))
    except OSError:
       pass
    
    file = open(os.path.join(RESULT_DIR, f_name.parent.with_suffix('.txt')), 'a')
    
    labels = np.loadtxt(txt_name)
    
    if len(labels.shape)==1:
        labels = np.expand_dims(labels,axis=0)
        
    Distribution_BBoxes_X = np.array(np.rint(labels[:,3] * X_image), dtype='uint')
    Distribution_BBoxes_Y = np.array(np.rint(labels[:,4] * Y_image), dtype='uint')
    
    # We keep the longer side of the bounding boxe
    Distribution_BBoxes = np.maximum(Distribution_BBoxes_X, Distribution_BBoxes_Y)
    
    for i in range(len(Distribution_BBoxes)):    
        file.write(str(Distribution_BBoxes[i]).zfill(4))
        file.write("\n")
    file.close()