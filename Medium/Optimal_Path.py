'''Instructions to candidate.
1) You are an avid rock collector who lives in southern California. Some rare 
        and desirable rocks just became available in New York, so you are planning
        a cross-country road trip. There are several other rare rocks that you could
        pick up along the way. 
        
        You have been given a grid filled with numbers, representing the number of
        rare rocks available in various cities across the country. Your objective
        is to find the optimal path from So_Cal to New_York that would allow you to
        accumulate the most rocks along the way. 
        
        Note: You can only travel either north (up) or east (right).
        
2) Consider adding some additional tests in doTestsPass().
3) Implement optimalPath() correctly.
4) Here is an example: 
            [[0,0,0,0,5], New_York (finish)     N
             [0,1,1,1,0],                   < W E >
    So_Cal (start) [2,0,0,0,0]] 
    
    The total for this example would be 10 (2+0+1+1+1+0+5). '''
    
def optimal_path(grid):
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    for row in range(len(grid)-1, -1, -1):
        for col in range(0, len(grid[0])):
            if row < len(grid)-1 and col > 0:
                grid[row][col] += max(grid(row+1](col], grid[row][col-1])
            elif row < len(grid)-1:
                grid[row][col] += grid[row+1][col]
            elif col > 0:
                grid[row][col] += grid[row][col-1]
    result = grid[0][len(grid[0])-1]
    print(result)
    return result 
    
def do_tests_pass():
    """ Returns True if all tests pass. Otherwise returns False. """
    test_inputs = [# Base test case 
    [[O, 0, 0, 0, 5], [0, 1, 1, 1, 0], [2, 0, 0, 0, 0]], 
# Random numbers 
[[1, 3, 2, 0, 2, 1, 8], [3, 4, 1, 2, 0, 1, 1], [1, 1, 1, 2, 3, 2, 1], [1, 0, 1, 1, 4, 2, 1]], 
# All 0's
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 
# Many optimal paths 
[[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]],
]
    
if __name__ =="__main__":
    if do_tests_pass():
        print('All tests pass')
    else:
        print('Not all tests pass')
        
