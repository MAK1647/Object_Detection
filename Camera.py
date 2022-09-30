# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 23:37:26 2022

@author: Admin
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
