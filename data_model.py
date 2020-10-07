#/usr/bin/python3
# @Author: Thomas Turner <thomas>
# @Date:   2020-09-23T11:50:37+02:00
# @Email:  thomas.benjamin.turner@gmail.com
# @Last modified by:   thomas
# @Last modified time: 2020-10-07T22:30:27+02:00

import numpy as np
import algorithm

class DataModel:
    '''
    Uses the algorithm set up in the algorithm class and creates the data to be
    interpreted and sent back to the user.

    Attributes:
    -----------
    None

    Methods:
    --------
    algorithm_frame(pointer, operation_list):
        Uses the algorithm_frame to do the moves and add each result of the move
        to a list.

    '''
    def algorithm_frame(pointer, matrix, operation_list):
        '''
        Does the algorithm.

        Parameters:
        -----------
        pointer : object
            The pointer object.


        operation_list : list
            The list of actions for the pointer object.

        Returns:
        --------
        moves_ : list
            List containing position vectors and direction integers.


        '''
        alg = algorithm.MovementAlgorithm()
        moves_ = [[pointer.position, pointer.heading]]
        for operation in operation_list:
            if operation !=0:
                alg.do_action(operation,pointer,matrix)
                moves_.append([pointer.position, pointer.heading])
            else:
                break

        return moves_
