
# Playing with Points
Playing with Points as a command line programme where the user enters in the dimensions of a matrix and the starting position of a point, then, a list of actions for the point to do and returns whether or not the point is in or outside of the matrix.


## Installation
Download the programme files to a local directory.

## Usage
Run the programme from the terminal in a python3 environment.

'''bash
python3 playing_with_points.py
'''

## Contributing

Please do! Pull requests are welcome. Please open an issue and discuss what changes you'd like to make first if they are seemingly large.

## More information:

The programme begins by first taking user input defining shape of the
space and the initial position of a point. Then it takes in a string of
numbers from 0-4 that defining the actions that the point can do.

The matrix is set up with the origin in the top left corner
```

  (0,0)               (0,n)
    -------------------
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    -------------------
   (m,0)              (m,n)
```

0: ends the movement and evaluates final position.
1: moves the point forward one step in the direction it is facing
(default direction is '0' or up)
2: moves the point backward one step in the direction it is facing
3: rotates the point 90 degrees to the right
4: rotates the point 90 degrees to the left

Once the inputs have been accepted the user will see if they have managed to
have the point end up in the matrix.
