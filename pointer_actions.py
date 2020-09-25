#/usr/bin/python3
# @Author: Thomas Turner <thomas>
# @Date:   2020-09-23T11:50:37+02:00
# @Email:  thomas.benjamin.turner@gmail.com
# @Last modified by:   thomas
# @Last modified time: 2020-09-25T13:57:30+02:00


import operator
import numpy as np

class PointerActions:
    '''
    The actions and movements the pointer can make.

    Attributes:
    -----------
    None

    Methods:
    --------

    get_correct_action(self,number):
        Contains list of actions and returns the correction action for the step.

    direction_scalar(self,direction):
        Reads the current direction modulo 360 and returns whether to move in the
        x or y direction, as well as a scalar to account for direction.

    rotate_pointer(self, action,pointer):
        Gets the current state and updates by + or - 90 degrees.

    move_one_step(self, x_y, scalar, action, pointer):
        Updates the position attribute of the pointer by moving in the correct
        direction taking into account the direction it is facing.

    '''

    def get_correct_action(self,number):
        '''
        Gets the correct action from the dictionary containing all possible
        moves.

        Parameters:
        -----------
        number : int
            The action specified by user for this step.

        Returns:
        --------
            The correct action to be performed.


        '''
        action_dict = {0: None, 1 : operator.sub, 2: operator.add, 3: 90, 4: -90}
        return action_dict.get(number)

    def direction_scalar(self,pointer):
        '''
        Uses the direction to determine if it moves in the x or y direction.
        Furthermore, it uses the position to determine how forward and backward
        movement should be scaled.

        Parameters:
        -----------
        pointer : object
            The pointer object.

        Returns:
        --------
        __scalar_dict.get(n), __x_y_dict.get(n) : int, ndarray
            The scalar accounting for direction facing, and the movement vector
            if it is in the x or y directions.

        '''
        x_move = np.array([1,0])
        y_move = np.array([0,1])

        direction = getattr(pointer, 'heading')
        __scalar_dict = {0 : 1, 90 : 1, 180 : -1, 270: -1}
        __x_y_dict = {0: x_move , 180 : x_move, 90 : y_move, 270 : y_move}
        return __scalar_dict.get(direction%360), __x_y_dict.get(direction%360)


    def rotate_pointer(self, action, pointer):
        '''
        Updates the pointer direction + or - 90 degrees.

        Parameters:
        -----------
        action : int
            Plus or minus 90 to be added to current pointer.heading attribute.

        pointer : object
            To access the pointer.heading attribute.

        Returns:
        --------
        None

        '''
        cur_heading = getattr(pointer,'heading')
        setattr(pointer,'heading', cur_heading + action)

    def move_one_step(self, x_y, scalar, action, pointer):
        '''
        Updates the pointer position vector.

        Parameters:
        -----------
        x_y : ndarray
            Vector determining if movement is in x or y direction.

        scalar : int
            Plus or minus one to scale the movement properly for direction.

        action : function
            Uses the operator add and sub functions based on forwards or
            backwards movement.

        pointer : object
            To access the pointer.position attribute.

        Returns:
        --------
        None
        
        '''
        cur_position = getattr(pointer,'position')
        setattr(pointer,'position', action(cur_position,(scalar*x_y)))
