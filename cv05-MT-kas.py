# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:32:09 2015

@author: Asus
"""

import numpy as np
import matplotlib.pyplot as plt
import struct, os, math, cv2

clear = lambda: os.system('cls')
clear()
plt.close('all')


with open('Cv05_LZW_data.bin', 'rb') as f:
    byte = f.read(1)
    print byte
    while byte != "":
        # Do stuff with byte.
        print byte        
        byte = f.read(1)