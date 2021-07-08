# 4 Problem Name is &&& Is Power of 10 &&& PLEASE DO NOT REMOVE THIS LINE. 
"""
Instructions to candidate.
1) Run this code in the REPL to observe its behaviour. The execution entry point is main().
2) Consider adding some additional tests in doTestsPass().
3) Implement isPower0110() correctly.
4) If time permits, some possible follow-ups.
"""
def isPowerOflO(x):
    """ Returns 1 if x is a power-of-10. Otherwise returns 0. """
    #todo: implement here return False
    i = 1
    
    if x > 1:
        while i < x:
            i *= 10
    
    elif x > 0:
        while i > x:
            i /= 10
    
    if i == x:
        return True
    return False

def doTestsPass():
    """ Returns 1 if all tests pass. Otherwise returns 0. """
    #todo: implement more tests, please
    #feel free to make testing more elegant
    doPass = True
    powersOf10 = [10]
    notPowersOf10 = [5]

    for n in powersOf10:
        if not isPowerOflO(n):
            print("Failed for " + str(n) + "\n")
            doPass = False

    for n in notPowersOf10:
        if isPowerOflO(n):
            print("Failed for " + str(n) + "\n")
            doPass = False

    if doPass:
        print("All tests pass\n")

    return doPass

if __name__ == "__main__":
    doTestsPass()