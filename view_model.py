#/usr/bin/python3
# @Author: Thomas Turner <thomas>
# @Date:   2020-09-23T11:50:37+02:00
# @Email:  thomas.benjamin.turner@gmail.com
# @Last modified by:   thomas
# @Last modified time: 2020-10-07T22:30:00+02:00

import pointer, matrix, data_model, validate_output

v_o = validate_output.ValidateOutput()

class ViewModel:
    '''
    Sets up the information that would be 'viewed' by the user.

    Attributes:
    -----------

    matrix : object
        a class object of matrix containing the (y,x)-ndarray of zeros

    pointer : object
        a pointer class object storing position and direction as Attributes


    '''

    def __init__(self, matrix_dim, start_pos):
        '''Initializes the class by creating pointer and matrix objects.'''
        self.matrix = matrix.MatrixObject(matrix_dim)
        self.pointer = pointer.PointerObject(start_pos)

    def __call__(self, ops_list):
        '''Moves the pointer around and validates end position. Returns the
        results to the user.'''
        move_list = data_model.DataModel.algorithm_frame(self.pointer, self.matrix, ops_list)
        data, message = v_o.check_end_position(move_list,self.matrix)
        return data, message
