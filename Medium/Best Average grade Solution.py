# Problem Name is &&& Best Average Grade &&& PLEASE DO NOT REMOVE THIS LINE. 

"""
Instructions: 
Given a list of student test scores, find the best average grade. Each student may have more than one test score in the list. 
Complete the bestAverageGrade function in the editor below. It has one parameter, scores, which is an array of student test scores. Each element in the array is a two-element array of the form [student name, test score] e.g. [ "Bobby", "87" ]. Test scores may be positive or negative integers. 
If you end up with an average grade that is not an integer, you should use a floor function to return the largest integer less than or equal to the average. Return 0 for an empty input. 

Example:
Input:
[ [ "Bobby", "87" ],
[ "Charles", "100" ], 
[ "Eric", "64" ], 
[ "Charles", "22" ] ].

Expected output: 87

Explanation: The average scores are 87, 61, and 64 for Bobby, Charles, and Eric, respectively. 87 is the highest. 
"""
import math 
""" Find the best average grade. """ 
def bestAverageGrade(scores): 
    # check for empty list
    if(len(scores) == 0): 
        return 0 
    # Build dictionary of students to tuple of running average and count 
    scoresByStudent = {} 
    for scoreRow in scores: 
        # check for well formed entry 
        if len(scoreRow)!=2: 
            return 0 
            
        student = scoreRow[0] 
        score = int(scoreRow[1]) 
        
        currentAvg = scoresByStudent.get(student,(0, 0))
        newAvg = (currentAvg[0] * currentAvg[1] + score) / (currentAvg[1] + 1) 
        scoresByStudent[student] = (newAvg, currentAvg[1] + 1) 
    scoresOnly = scoresByStudent. values() 
    averages = map(lambda x: x[0], scoresOnly) 
    return int(math.floor(max(averages))) 
    
def doTestsPass():
    """ Returns true if the tests pass. Otherwise, returns false """ 
    testCases = [
            # example
            
            ([ [ "Bobby", "87" ], 
                    [ "Charles", "100" ], 
                    [ "Eric", "64" ], 
                    [ "Charles", "22" ] ], 87),
            # empty 
            
            ([], 0),
                        
            # multiple scores each 
                    
            ([ [ "Sarah", "91" ], 
            [ "Goldie", "92" ],
            [ "Elaine", "93" ], 
            [ "Sarah", "93" ],
            [ "Goldie", "94" ]],  93),
            
            
              
            # negatives and zeros 
            ([  
                
                ["Janie",  "-66" ],
                ["Janie",  "0" ], 
                [ "Gina", "-88" ], 
                [ "Bobby", "0" ], 
                [ "Gina", "44" ], 
                [ "Bobby", "-6" ],
                [ "Bobby", "-6" ]], -4),
                 
             
            # same value and average 
            ([  [ "Alpha", "99" ], 
                ["Bravo", "99" ],
                ["Charlie","99"],
                ["Delta", "99" ],
                ["Echo", "99" ], 
                ["Foxtrot", "99" ],
                ["Foxtrot", "99" ]],99),
                
            # non-integer average 
            ([  [ "Gerald", "91" ],
                [ "Gerald", "92" ] ], 91), 
                
            # negative non-integer average 
            ([  [ "Barry", "-66" ], 
                [ "Barry", "-65" ],
                [ "Alfred", "-122"] ], -66) 
                
            ] 
    passed = True 
    for tc, expected in testCases:
        actual = bestAverageGrade(tc) 
        if actual != expected: 
            passed = False 
            print("Failed for case ", tc, "\n expected ", expected, ", actual ", actual) 
            return passed 
        else:
            return passed
            
if __name__ == "__main__":
    result = doTestsPass() 
    if result: 
        print("All tests pass\n"); 

