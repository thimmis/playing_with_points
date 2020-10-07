#/usr/bin/python3
# @Author: Thomas Turner <thomas>
# @Date:   2020-10-07T20:43:48+02:00
# @Email:  thomas.benjamin.turner@gmail.com
# @Last modified by:   thomas
# @Last modified time: 2020-10-07T23:14:18+02:00

import pointer_actions
import operator
from math import cos, sin, radians
import numpy as np

class MatrixActions:
    '''
    The actions that be done to rotate the space(matrix).

    Attributes:
    ----------
    None

    Methods:
    --------
    rotate_matrix(self, pointer, matrix, degree):
        General function for rotating the "space" and the point about the space.
        ASSUMTION: that the matrix is rotated around the origin point

    '''

    def rotate_matrix(self, degree, pointer, matrix):
        p_act = pointer_actions.PointerActions()
        cur_orientation = getattr(matrix,'orientation')
        #update the matrix orientation to help determine where points lie
        if degree == 90:
            setattr(matrix,'orientation',cur_orientation+1)
        if degree == -90:
            setattr(matrix,'orientation',cur_orientation-1)
        #develop the appropriate rotation matrix
        rotation = rot_mat = np.array([[cos(radians(degree)),sin(radians(degree))],
                                        [-sin(radians(degree)),cos(radians(degree))]])
        #rotate the pointer position and direction facing
        setattr(pointer,'position',np.dot(rotation,getattr(pointer,'position')))
        p_act.rotate_pointer(degree,pointer)
        #get the 3 moving points and rotate them
        top_r = getattr(matrix,'top_right')
        bot_l = getattr(matrix, 'bottom_left')
        bot_r = getattr(matrix,'bottom_right')
        setattr(matrix,'top_right',np.dot(rotation,top_r))
        setattr(matrix,'bottom_right',np.dot(rotation,bot_r))
        setattr(matrix,'bottom_left',np.dot(rotation,bot_l))
