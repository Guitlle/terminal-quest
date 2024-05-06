#!/usr/bin/env python

# paths.py
#
# Copyright (C) 2014-2019 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#

'''
Discovers and exposes the absolute pathnames for common_css_dir and common_images_dir
'''

import os

# setting up directories
dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# media dir
media_local = os.path.join(dir_path, 'app-data', 'kano', 'media')
common_media_dir = media_local
common_css_dir = os.path.join(common_media_dir, 'CSS')
common_images_dir = os.path.join(common_media_dir, 'images')
