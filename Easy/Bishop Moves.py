# Problem Name is &&& Bishop Moves &&& PLEASE DO NOT REMOVE THIS LINE. 

"""
Instructions to candidate. 

1) Run this code in the REPL to observe its behaviour. The 
    execution entry point is main(). 
2) Implement bishop_moves(src,dest) correctly. Assume src, dest are strings 
3) Consider adding some additional tests in doTestsPass(). 
4) If time permits, some possible follow-ups. 
"""
"""
You are shipwrecked on an island. You have lost all your possessions 
save a single standard chess board (8x8) and two soggy playing 
pieces - a bishop and a seashell. 

Recall that the bishop is limited to diagonal movement, but has
no restrictions in 1-d distance traveled for each move. 
The seashell cannot move once placed. To pass the time you invent 
a new chess-like game that works as follows: 
1. Place the seashell at any location on the board. 
    The shell does not move after being placed.
2. Place the bishop at any location on the board.
3. Using only legal moves, capture the seashell using the bishop.

Write a function that takes as input the coordinates of the 
seashell and the bishop, with 1-8 labeling rows and A-H labeling columns
and returns the number of moves { 0, 1, 2, ... } it takes to capture 
the seashell using the bishop. Return -1 if this is not possible.
"""
def bishop_moves(src, dest):
    if( src == dest ): 
        return 0 
    if(abs(ord(src[0])-ord(dest[0]))==abs(ord(src[1])-ord(dest[1]))):
        return 1 
    if((ord(src[0])+ord(src[1]))%2 ==(ord(dest[0])+ord(dest[1]))%2): 
        return 2 
    return -1 
""" Returns True if all tests pass. Otherwise returns False """ 
def doTestsPass(): 
    test = [ 
            [ "A1", "C3" ],
            [ "A1", "D6" ] 
        ]
    solutions = [ 1, 2 ] 
    allTestsPass = True; 
    for i in range(len(test)): 
        print("Running test", i+1 ) 
        actual = solutions[i] 
        expected = bishop_moves(test[i][0], test[i][1]) 
        allTestsPass = allTestsPass and (actual == expected) 
        if actual != expected: 
            print("Failed on test", i+1) 
    return allTestsPass 
            
if __name__ == "__main__":
    if(doTestsPass()): 
        print("All tests pass") 
    else: 
        print("There are test failures") 


