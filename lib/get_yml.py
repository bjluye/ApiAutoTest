# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__:'luye'

import os
import yaml

def get_yml_data(yml):
    parent_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    path = parent_path+'\data/\/'+yml
    with open(path,encoding='utf-8') as f:
        temp = yaml.load(f.read())
        return temp
