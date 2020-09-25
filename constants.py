#/usr/bin/python3
# @Author: Thomas Turner <thomas>
# @Date:   2020-09-24T11:00:36+02:00
# @Email:  thomas.benjamin.turner@gmail.com
# @Last modified by:   thomas
# @Last modified time: 2020-09-25T14:39:53+02:00

import textwrap as tw

class Constants:
    '''
    The generic messages to be printed to the user.

    Attributes:
    -----------
    None

    Methods:
    --------
    start_message(self):
        The starting message user sees.

    action_list_message(self):
        Message sent to user regarding input of actions.


    '''
    def start_message(self):
        '''
        Parameters:
        -----------
        None

        Returns:
        --------
        None

        '''
        message =tw.fill("""Start by entering in the dimensions of the matrix you wish to traverse followed by a comma followed by the point at which you would like to start e.g. '4,4,2,2'""", width = 55)
        print(message)

    def action_list_message(self):
        '''
        Parameters:
        -----------
        None

        Returns:
        --------
        None

        '''
        message =tw.fill("""Tell the point how you want it to move by giving it a list of numbers from 0-1. '1' tells the point to move forward 1 step in the direction it is facing (default is up). '2' tells the point to move backwards one step facing the same direction. '3 & 4' tell the point to rotate 90 degrees to the right and left, respectively. '0' tells the point to stop moving and evaluate position, will auto-append one to the end if please enter numbers from 0-4 separated by comma here: """,width=55)
        print(message)
