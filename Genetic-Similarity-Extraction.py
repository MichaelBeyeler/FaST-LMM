# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 23:08:41 2017

@author: micha
"""

import os
import numpy as np
os.chdir('../FaST-LMM-master')


tmp1 = np.load('Gimme-Cache.1.npz')
tmp2 = np.load('Gimme-Cache.2.npz')
tmp3 = np.load('Gimme-Cache.3.npz')
tmp4 = np.load('Gimme-Cache.4.npz')

mycache = np.load('Cache-Data-All-Lines-Leave-Out-One.6.npz')
