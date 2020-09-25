#/usr/bin/python3
#@Author: Thomas Turner <thomas>
#@Date:   2020-09-23T11:12:09+02:00
#@Email:  thomas.benjamin.turner@gmail.com
# @Last modified by:   thomas
# @Last modified time: 2020-09-25T14:51:18+02:00


import sys, validate_input, view_model, constants


class PointMoverCmd:
    '''
    The class that the user interacts with to set up the matrix dimensions,
    starting position of the pointer and the list of actions that the pointer
    will take.

    Attributes:
    -----------
    vi : object
        validate_input class object for ensuring user input is correct.

    cc : object
        constants class object to give user generic messages containing
        instructions.

    dim : list
        [x,y] defining shape of the matrix split from position

    pos : list
        [x,y] defining the starting position of the pointer split from matrix

    actions : list
        validated list of actions to be sent to sent to the data model for
        moving the pointer around.

    view_mod : object
        class object of the view_model that sets up the pointer and matrix

    results , message : list, str
        the result of the pointer's final position and corresponding message to
        be sent back to the user.


    Methods:
    --------

    None
    '''
    vi = validate_input.ValidateInput()
    cc = constants.Constants()


    cc.start_message()
    dim, pos = vi.split_input(vi.check_dimension_position(sys.stdin.readline().rstrip()))
    cc.action_list_message()
    actions = vi.contains_zero(vi.check_operation_list())
    view_mod = view_model.ViewModel(dim, pos)
    result, message = view_mod(actions)

    sys.stdout.write(message.format(result))
