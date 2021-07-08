# Problem Name is &&& Staircase &&& PLEASE DO NOT REMOVE THIS LINE. 
''' 
    Instructions: 
    There is a staircase with 'n' number of steps. A child
    walks by and wants to climb up the stairs, starting at
    the bottom step and ascending to the top.
    
    Of course, the child wants to have fun, too, so instead
    of taking 1 step at a time, she will vary between taking
    either 1, 2 or 3 steps at a time.
    
    Please complete the 'countSteps' method below so that
    given 'n' number of steps it will return the number of
    unique combinations the child could traverse. 
    
    An example would be countSteps(3) == 4: 
    
    1 1 1
    2 1
    1 2
    3
'''

''' Given n steps, returns the number of possible permutations
        to climb the staircase.
    Returns 0 when the input n is <= 0.'''
# Naive exponential solution
def countSteps(n):
    if n <= 0:
        return 0; 
    return countStepsRec(n) 

def countStepsRec(n):
    if n == 0:
        return 1
    if n < 0:
        return 0; 

    return countStepsRec(n - 1) + countStepsRec(n - 2) + countStepsRec(n - 3) 
'''
# Iterative linear solution
def countSteps(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4 
        
    counts = [0, 1, 2, 4] 
    
    for i in range(4, n+1):
        counts.append(counts[i - 1] + counts[i - 2] + counts[i - 3]) 
    
    return counts[n] 
'''
'''
# Memoized solution 
memoized = {}
def countSteps(n):
    if n <= 0:
        return 0; 
    return countStepsRec(n) 

def countStepsRec(n):
    if n == 0:
        return 1
    if n < 0:
        return 0; 
    if n in memoized:
        return memoized[n] 

    count = countStepsRec(n - 1) + countStepsRec(n - 2) + countStepsRec(n - 3)
    memoized[n] = count
    return count 
'''

'''
# Memoized via function decoration (only works in Python 3)
def countSteps(n):
    if n <= 0:
        return 0
    return countStepsRec(n) 

from functools import lru_cache
@lru_cache()
def countStepsRec(n):
    if n == 0:
        return 1
    if n < 0:
        return 0; 
    return countStepsRec(n - 1) + countStepsRec(n - 2) + countStepsRec(n - 3) 
'''
def doTestsPass():
    '''Returns 1 if the tests pass. Otherwise, returns 0;'''
    # todo: implement more tests, if you'd like
    return (countSteps(3) == 4
            and countSteps(4) == 7
            and countSteps(1) == 1
            and countSteps(2) == 2
            and countSteps(0) == 0
            and countSteps(-5) == 0
            and countSteps(10) == 274
            and countSteps(36) == 2082876103) # Will cause naive solution to time-out 
            
if __name__ == "__main__":
    result = doTestsPass() 
    if result: 
        print("All tests pass\n");
    else:
        print("Tests fail\n"); 
    for i in range(5):
        print("%d steps => %d\n" % (i + 1, countSteps(i + 1))); 















