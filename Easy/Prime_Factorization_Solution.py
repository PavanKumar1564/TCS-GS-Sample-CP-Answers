#Instructions to candidate.
"""
1) Run this code in the REPL to observe its behaviour. The execution entry point is main().
2) Consider adding some additional tests in doTestsPass().
3) Implement primeFactorization() correctly.
4) If time permits, some possible follow-ups. 
"""

"""
Return an array containing prime numbers whose product is x
    Examples: 
        primeFactorization(6) == [2,3]
        primeFactorization(5) == [5]
        primeFactorization(12) == [2,2,3]
"""

def primeFactorization(x):
    # todo: implement here return []
    if x < 1:
         return
    factors = []
    i = 2
    
    while i <= x:
        while x % i == 0:
            x /= i
            factors.append(i)
        i += 1

    return factors

def doTestsPass():
    """ Returns True if all tests pass. Otherwise returns False. """
    testVals = [6, 5, 12, 1, -1]
    testAnswers = ([2, 3], [5], [2, 2, 3], [], None)

    for value, answer in zip(testVals, testAnswers):
        if primeFactorization(value) != answer:
            print ("Test failed for %d" % value)
            return False
    return True

if __name__ == "__main__":
    if doTestsPass():
        print ("All tests pass")
    else:
        print ("Not all tests pass")