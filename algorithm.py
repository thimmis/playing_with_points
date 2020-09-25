# @Author: Thomas Turner <thomas>
# @Date:   2020-09-24T18:06:58+02:00
# @Email:  thomas.benjamin.turner@gmail.com
# @Last modified by:   thomas
# @Last modified time: 2020-09-25T14:44:16+02:00



import pointer_actions



class MovementAlgorithm:
    '''
    Splits movement into 4 cases. Will perform the corresponding action when
    given that particular action.

    Attributes:
    -----------
    None

    Methods:
    --------
    do_action(self, number, pointer):
        Performs the actions and updates the pointer object attributes.

    '''
    def do_action(self, number, pointer):
        '''
        Takes a single number and the pointer and updates the attributes based
        on which number was given.

        Parameters:
        -----------
        number : int
            An integer defining which action to do.

        pointer : object
            The pointer object.

        Returns:
        --------
        None

        '''
        p_act = pointer_actions.PointerActions()
        action = p_act.get_correct_action(number)
        scalar, x_y = p_act.direction_scalar(pointer)
        if number ==1:
            p_act.move_one_step(x_y, scalar, action, pointer)
        if number == 2:
            p_act.move_one_step(x_y, scalar, action, pointer)
        if number ==3:
            p_act.rotate_pointer(action,pointer)
        if number ==4:
            p_act.rotate_pointer(action,pointer)
