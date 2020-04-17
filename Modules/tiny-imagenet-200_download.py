# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SBXmtI6mCk9J_YIZPUn0Hdj96Hg13Aw4
"""

import os
import zipfile
import requests
from io import StringIO,BytesIO
def download_images(url):
    
    
    if (os.path.isdir("tiny-imagenet-200.zip")):
        print('Images already downloaded...')
        return
    r=requests.get(url,stream=True)
    print('Downloading' + url)
    zip_ref=zipfile.ZipFile(BytesIO(r.content))
    zip_ref.extractall('./')
    zip_ref.close()
download_images("http://cs231n.stanford.edu/tiny-imagenet-200.zip")