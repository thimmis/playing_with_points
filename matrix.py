#/usr/bin/python3
# @Author: Thomas Turner <thomas>
# @Date:   2020-09-23T11:50:37+02:00
# @Email:  thomas.benjamin.turner@gmail.com
# @Last modified by:   thomas
# @Last modified time: 2020-09-25T14:03:39+02:00

import numpy as np

class MatrixObject:
    '''
    Sets up the matrix object for evaluating final position of the pointer.

    Currently under utilized and not entirely necessary as we can do this abstractly.

    Attributes:
    -----------
    matrix : ndarray
        A matrix with dimensions specified by user input.

    Methods:
    --------
    None

    '''
    def __init__(self,dimensions):
        ''' Sets up the matrix object. '''
        #numpy indexes COLUMN size then ROW size --> switch position of x and y input
        self.matrix = np.zeros((dimensions[1],dimensions[0]))
