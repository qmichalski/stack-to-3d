# -*- coding: utf-8 -*-
"""
Created on Thu May 11 07:13:03 2023

@author: quent
"""

from evtk import hl
import numpy as np
import cv2
import glob

firstFile = glob.glob(".\\images\\*.tif")[0]
img=cv2.imread(firstFile)

zMax = 0
for file in glob.glob(".\\images\\**.tif"):
    bname = file.split('_')
    zMax = int(np.max([int(bname[1].split('z')[1]),zMax]))
zMax = zMax + 1

x = np.arange(0,img.shape[0]+1, dtype=np.int32)
y = np.arange(0,img.shape[1]+1, dtype=np.int32)
z = np.arange(0,zMax+1, dtype=np.int32)

ic = 3 # number of color in the initial image
valStack = np.zeros((img.shape[0],img.shape[1],zMax,ic))

for file in glob.glob("*.tif"):
    bname = file.split('_')
    c = int(bname[2].split('.')[0].split('c')[1])
    iz = int(bname[1].split('z')[1])
    img=cv2.imread(file)
    valStack[:,:,iz,c-1] = img[:,:,0]

path = './/3d_stack'
hl.gridToVTK(path,
            x = x, 
            y = y,
            z = z, 
            cellData= dict(C1=np.ascontiguousarray(valStack[:,:,:,0]),
                           C2=np.ascontiguousarray(valStack[:,:,:,1]),
                           C3=np.ascontiguousarray(valStack[:,:,:,2])))