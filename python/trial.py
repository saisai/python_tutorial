#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

# A tuple containing the five components of the version number: major, minor, micro, releaselevel, and serial.
print sys.version_info

print os.path.join('share', 'pixmaps')

# os.path.abspath取得文件
app_root = os.path.split(os.path.abspath(sys.argv[0]))[0]
print sys.argv
print os.path.abspath(sys.argv[0])
print app_root

