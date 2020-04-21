#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:02:35 2020

@author: craffaelli
"""

import numpy as np

dropped_list_NOLOOPS = np.array([[ 0, 23,  0, -1,  0],
        [ 2, 56,  0, -1,  0],
        [ 5, 25,  1,  0,  0],
        [12, 26,  0,  0, -1],
        [15, 55,  0,  1,  0],
        [15, 75,  0,  1,  0],
        [21, 64,  0,  0, -1],
        [26, 42,  1,  0,  0],
        [28,  2,  0,  1,  0],
        [33, 58, -1,  0,  1],
        [38, 51, -1,  0,  0],
        [39, 19,  0,  0,  1],
        [45, 22,  0,  0, -1],
        [48, 65,  0,  0,  1],
        [50, 65,  0,  0,  1]])


dropped_list1 = np.array([[ 1, 8,  0, -1,  0],
        [ 2, 8,  0, -1,  0],
        [ 3, 4,  1,  0,  0],
        [5, 2,  0,  0, -1],
        [6, 2,  0,  0,  -1],
        [8, 6,  0,  0,  1],
        [8, 9,  0,  0, 1],
        [8, 10,  0,  0,  1],
        [9,  2,  0,  0,  -1]])


# odd cases (see powerpoint)
A = np.array([[ 1, 2,  -1, 0,  0],
        [ 2, 3,  1, 0,  0],
        [3,  1,  1,  0,  0]])

B = np.array([[ 1, 2,  1, 1,  0],
        [ 1, 4,  1, 0,  0],
        [ 1, 7,  1,  0,  0],
        [2, 3,  1,  1, 0],
        [2, 3,  -1,  -1,  0],
        [3, 4,  0,  1,  0],
        [4, 1,  0,  -1, 0],
        [4, 5,  0,  -1, -1],
        [5,  3,  0,  1,  0],
        [5, 6, 1,  1,  1],
        [6, 7, 0,  -1,  -1],
        [7, 2,  1,  0,  0],
        [7, 8,  0,  0, -1],
        [8, 5,  0,  -1,  0],
        [8, 9,  0,  0,  1]])


dropped_list = B