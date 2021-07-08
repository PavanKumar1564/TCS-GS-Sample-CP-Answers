# Problem Name is &&& Walking Robot &&& PLEASE DO NOT REMOVE THIS LINE. 
# Instructions to candidate # 1. Run this code in the REPL to observe its behaviour. The • execution entry point is main().
# 2. Implement the 'walk' method. This method takes in a string, path, • where each character in the string corresponds to a potential movement • of the robot. The robot can move up, down, left, and right represented • by the characters 'U', 'D', 'L', and 'R' respectively. All other • characters may be ignored. Assume the robot's initial position • is at (0,0). The output of this method is the robot's final x and y • coordinates relative to the initial position.
# 3. Consider adding more test cases 
def walk( path ):
    # TODO: Implement solution return( [0,0] )
    ret = [0,0]
    directions = {"U" : [ 0, 1], "D" : [ 0,-1], "L" : [-1, 0], "R" : [ 1, 0] }
    for char in path:
        ret = [ a + b for a, b in zip( ret, directions.get( char, [0,0] ) ) ]
    return( ret )

def do_tests_pass():
    """ Returns True if all tests pass. Otherwise returns False. """
    """# TODO: implement some tests, please # we've included a trivial boilerplate """
    # path, expected
    test_cases = [ "UUU", [0, 3] ], [ "ULDR", [0, 0] ], [ "ULLLDUDUURLRLR", [-2,2] ], [ "UP LEFT 2xDOWN DOWN RIGHT RIGHT UP UP", [1,1] ]
    result = True
    for test in test_cases:
        result = result and ( walk( test[0] ) == test[1] )
    if result:
        print("Test passed.")
        return True
    else:
        print("Test failed.")
        return False

if __name__ == "__main__":
    do_tests_pass()