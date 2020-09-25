#/usr/bin/python3
#@Author: Thomas Turner <thomas>
#@Date:   2020-09-23T11:12:09+02:00
#@Email:  thomas.benjamin.turner@gmail.com
# @Last modified by:   thomas
# @Last modified time: 2020-09-25T13:57:55+02:00

import numpy as np

class PointerObject:
    '''
    The pointer object class to be updated by the data model.

    Attributes:
    -----------
    position : ndarray
        numpy array containing starting x and y positions [x,y].

    heading : int
        Value to be read (modulo 360) to determine which direction it is facing.

    Methods:
    --------
    None

    '''
    def __init__(self,start_pos):
        ''' Initializes the object with the position defined by user. '''
        self.position = np.array([start_pos[0],start_pos[1]])
        self.heading = 0 #default position.
