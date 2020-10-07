#/usr/bin/python3
# @Author: Thomas Turner <thomas>
# @Date:   2020-09-24T18:53:56+02:00
# @Email:  thomas.benjamin.turner@gmail.com
# @Last modified by:   thomas
# @Last modified time: 2020-10-07T22:58:28+02:00

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

        matrix : object
            the matrix object containing the orientation and corner data of the
            target space.

        Returns:
        --------
        data_out : list
            [-1,-1] if the point is outside the matrix or the final position


        message_out : str
            one of two message whether or not the point is inside or outside of
            the matrix at the final position.



        '''
        final_orientation = matrix.orientation
        final_pos = move_list[-1][0]

        if final_orientation%4 == 0:
            x_in_out = ( 0 < final_pos[0] < matrix.top_right[0])
            y_in_out = ( 0 < final_pos[1] < matrix.bottom_right[1])

        if final_orientation%4 == 1:
            x_in_out = (matrix.bottom_left[0] < final_pos[0] < 0)
            y_in_out = (0 < final_pos[1] < matrix.top_right[1])

        if final_orientation%4 == 2:
            x_in_out = (matrix.bottom_right[0] < final_pos[0] < 0)
            y_in_out = (matrix.bottom_right < final_pos[1] < 0)

        if final_orientation%4 == 3:
            x_in_out = (0 < final_pos[0] < matrix.bottom_left[0])
            y_in_out = (matrix.top_right[1] < final_pos[1] < 0)

        if (x_in_out or y_in_out) == False:
            data_out = [-1,-1]
            message_out = '{} Point outside of boundary, better luck next time!\n'
        else:
            data_out = [final_pos[0],final_pos[1]]
            message_out = '{} Coungrats! You managed to end up inside of the matrix.\n'
        return data_out, message_out
