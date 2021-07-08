# Problem Name is &&& Snowpack &&& PLEASE DO NOT REMOVE THIS LINE. 
'''
 Instructions to candidate.
    1) Given an array of non-negative integers representing the elevations 
        from the vertical cross section of a range of hills, determine how
        many units of snow could be captured between the hills. 
        
        See the example array and elevation map below. 
        
                                                                 ___
                        ___                |   |        ____
                       |   |        ___    |   |___    |    |
                ___|   |    ___|   |   |   |   |   |   |
        ___|___|___|___|___|___|___|___|___|___|___|___
        [0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0]
        
                                                                 ___
                        ___                |   |        ____
                       |   | *   *  _*_  * |   |_*_  * |    |
                ___|   | *  _*_|   | * |   |   | * |   |
        ___|___|___|_*_|___|___|_*_|___|___|_*_|___|___
        [0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0]
        
        Solution: In this example 13 units of snow (*) could be captured. 
    2) Consider adding some additional tests in doTestsPass(). 
    3) Implement computeSnowpack() correctly. 
'''
def computeSnowpack(arr): 
    #Check for empty array 
    if(len(arr) == 0):
        return 0;
    total = 0 
    left_highest = [0 for i in range(len(arr))] 
    left_max = 0 
    for i in range(len(arr)): 
        if arr[i] > left_max: 
            left_max = arr[i] 
        left_highest[i] = left_max 
    right_max = 0 
    for i in reversed(range(len(arr))):
        if arr[i] > right_max: 
            right_max = arr[i] 
        if min(right_max, left_highest[i]) > arr[i]:
            total += min(right_max, left_highest[i]) - arr[i]
    print(arr, total) 
    return total 

def doTestsPass(): 
    """ Returns True if all tests pass. Otherwise returns False. """
    tests = [[[0,1,3,0,1,2,0,4,2,0,3,0], 13],
            [[1,0,0,0,0,0,0,0,0,0,0,1], 10],
            [[0,0,0,0,0], 0], 
            [[0,0,1,0,0], 0],
            [[1], 0],
            [[], 0]]
    for test in tests:
        if not (computeSnowpack(test[0]) == test[1]):
            return False 
    return True 

if __name__ =="__main__":
    if(doTestsPass()):
        print("All tests pass")
    else:
        print("Not all tests pass")
