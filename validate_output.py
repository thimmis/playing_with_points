#/usr/bin/python3
# @Author: Thomas Turner <thomas>
# @Date:   2020-09-24T18:53:56+02:00
# @Email:  thomas.benjamin.turner@gmail.com
# @Last modified by:   thomas
# @Last modified time: 2020-09-25T13:24:16+02:00

import numpy as np

class ValidateOutput:
    '''
    Takes in the list of actions and looks at the final x and y values and looks
    to see if they are in or outside of the matrix.

    Methods:
    --------
    check_end_position(self,move_list,matrix):
        Evaluates the final position

    '''

    def check_end_position(self,move_list,matrix):
        '''
        Looks at the last entry of the move_list and determines the correct
        information and message to be returned to the user.

        Parameters:
        -----------
        move_list : list
            list of moves made by the pointer

        matrix : ndarray
            the matrix set up by the user

        Returns:
        --------
        data_out : list
            [-1,-1] if the point is outside the matrix or the final position


        message_out : str
            one of two message whether or not the point is inside or outside of
            the matrix at the final position.



        '''
        x , y = matrix.matrix.shape[1], matrix.matrix.shape[0]
        final_pos = move_list[-1][0]

        x_in_out = (final_pos[0] < 0 or final_pos[0]> x)
        y_in_out = (final_pos[1] < 0 or final_pos[1] >y)

        if (x_in_out or y_in_out) == True:
            data_out = [-1,-1]
            message_out = '{} Point outside of boundary, better luck next time!\n'
        else:
            data_out = [final_pos[0],final_pos[1]]
            message_out = '{} Coungrats! You managed to end up inside of the matrix.\n'
        return data_out, message_out
