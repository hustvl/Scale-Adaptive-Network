# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""Set up paths for Multi-column."""

import os.path as osp
import sys


def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

this_dir = osp.dirname(__file__)

# Add caffe to PYTHONPATH
caffe_path = osp.join(this_dir, '..', '..', '..', 'pycaffe-balance')
#caffe_path = 'D:\\v-zihuan\\deeplabv2_to_new_caffe\\caffe-windows\\Build\\x64\\Release\\pycaffe'
add_path(caffe_path)

# Add lib to PYTHONPATH
lib_path = osp.join(this_dir, '.')
add_path(lib_path)
