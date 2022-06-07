import random

# lets create a board object to represent the minesweeper game
# this is so that we can just say "Create a new board object", or
# "dig here", or "render this game for this object"


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function
        self.board = self.make_new_board()  # plant the bombs

        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row,col) tuples into this set
        self.dug = set()  # if we dig at 0,0 then self.dug = {(0,0)}

    def make_new_board(self):
        # construct a new board based on the size on the dim size and num bombs
        # we should construct the list of lists here (or whatever representation you prefer)
        # but since we have a 2-D board, list of lists is most natural

        # generate a new board
        board = [[None for _ in range(self.dim_size)]
                 for _ in range(self.dim_size)]
        # this creates an array like this:
        # [[None, None,....,None],
        # [None, None,....,None],
        # [None, None, ...., None]]

        # plants the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                # this means we've actually planted a bomb there so keep going
                continue

            board[row][col] = '*'
            bombs_planted += 1


def play(dim_size, num_bombs=10):
    # Step 1: Create the board and plant the bombs
    # Step 2: Show the user the board and ask for where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb. dig recursively untill each square is at least next to a bomb
    # Step 4: Repeat step 2 and 3a/b untill there are no more places to dig -> VICTORY
    pass
