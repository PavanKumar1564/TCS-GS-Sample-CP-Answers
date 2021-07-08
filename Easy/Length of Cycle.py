# Problem Name is &&& Count Length Of Cycle &&& PLEASE DO NOT REMOVE THIS LINE. 
"""
Instructions to candidate.
1) Run this code in the REPL to observe its behaviour. The 
    execution entry point is main. 
2) Consider adding some additional tests.
3) Implement count_length_of_cycle() correctly. 
4) If time permits, some possible follow-ups. 

"""

"""
countLengthOfCycle(arr, start_index) 

You are given an integer array of size N. 
Every element of the array is greater than or equal to 0. 
Starting from arr[start_index], follow each element to the index it points to. 
Continue to do this until you find a cycle. 
Return the length of the cycle. If no cycle is found return -1 

Examples: 
countLengthOfCycle([1, 0], 0) == 2 
countLengthOfCycle([1, 2, 0], 0) == 3 
"""
def count_length_of_cycle(arr, start_index):
    visited = {} 
    count = 1 
    index = start_index 
    while(visited.get(index) is None): 
        if(arr[index] > len(arr)):
            return -1 
        visited[index] = count; 
        count+=1 
        index = arr[index]; 
    print(visited)
    return count - visited[index]; 
    
""" 
Returns True if all tests pass. Otherwise returns False. 
TODD: We've implement a simple test harness here. Feel free to add more tests and improve.
"""

def do_tests_pass():


    test_cases = [ 
        [[1, 0], 0, 2],
        [[1, 2, 0], 0, 3], 
        #additional test cases 
        # [[1, 1], 0, 1],
        # [[1, 3, 0, 1], 0, 2],
        # [[7], 0, -1],
        #[[1, 2, 4], 0, -1],
        ]
      
    tests_passed = True 
    for test_case in test_cases: 
            tests_passed &= count_length_of_cycle(test_case[0], test_case[1]) == test_case[2] 
    if tests_passed:
        print("Test passed.") 
        return True 
    else: 
        print("Test failed.") 
        return False 
if __name__ == "__main__": 
    do_tests_pass() 
