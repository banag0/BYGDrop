# -*- coding: utf-8 -*-
"""
@author: GB269667

Before putting the weigths on Github we devided each .pt file into two .pt file in order to be able to put them on Github. 
This code allows to merge the split .pt files and reconstruct the originals .pt files.
"""

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from filesplit.merge import Merge

merge = Merge(r"../YOLO_weights_dark_texture_split", "./", "dark_texture.pt")
merge.merge(cleanup = True)

merge = Merge(r"../YOLO_weights_light_texture_split", "./", "light_texture.pt")
merge.merge(cleanup = True)