# Problem Name is &&& Knight Probability &&& PLEASE DO NOT REMOVE THIS LINE. 

"""

Instructions: 

Given an empty chessboard (8x8 grid), a knight is placed
on one of the squares. The knight 'K' at position (3, 3)
and it's possible movements 'X' are shown in the example 
below: 

        ********
        **X*X***
        *X***X**
        ***K****
        *X***X**
        **X*X***
        ********
        ********

Depending on the knight's position on the board, 0-6 of 
the 8 possible movements may cause the knight to leave 
the chess board. 

If the knight moves n times, each time choosing one of
the 8 possible moves uniformly at random, determine the 
probability that the knight is still on the board after
making n random moves. After the knight has left the 
board, it may not reenter. 

Please implement the method probability which given a 
start position x, y, and a number of moves n, 
returns the probability a knight remains on the board 
as described above. 
"""
def probability(x, y, n): 
    board_size = 8 
    #Define an 8x8 grid 
    board = [[0.0 for r in range(board_size)] for r in range(board_size)]
    #Set the starting position
    board[x][y] = 1.0 
    for i in range(n):
        next_board = [[0.0 for r in range(board_size)] for r in range(board_size)] 
            #Fill in probabilties for every square on the previous board 
        for current_x in range(board_size): 
                for current_y in range(board_size): 
                    #Check all the board positions that could have lead here 
                    for move in [(-2, -1), (-2, 1), (2, -1), (2, 1),
                            (-1, -2), (-1, 2), (1, -2), (1, 2)]: 
                        previous_x = current_x + move[0] 
                        previous_y = current_y + move[1] 
                        if 0 <= previous_x < board_size and 0 <= previous_y < board_size: 
                            #Probability of getting to x, y is 1/8 * probability it was on previous square 
                            if board[previous_x][previous_y] > 0: 
                                next_board[current_x][current_y] += board[previous_x][previous_y] / 8 
        board = next_board 
        #Returns sum of all probabilities on the board 
    return sum(sum(s) for s in board) 
def do_tests_pass(): 
    #Returns True if the tests pass. Otherwise, returns False 
    test_cases = {
        #Start in a corner, no moves 
        (0, 0, 0): 1.0, 
        #Start in the middle, one move 
        (3, 3, 1): 1.0, 
        #Start in a corner, one move 
        (0, 0, 1): 0.25, 
        (0, 0, 2): 0.1875, 
        (1, 2, 10): 0.0522148497402668,
    }
    # todo: feel free to enhance or add more test cases 
    for case, expected in test_cases.items():
        if probability(case[0], case[1], case[2]) != expected: 
            return False
        return True 
        
if __name__ == "__main__": 
    
    if do_tests_pass(): 
        print("All tests pass")
    else: 
        print("Tests fail")

