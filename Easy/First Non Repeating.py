"""
Instructions to candidate. 
    1) Run this code in the REPL to observe its behaviour. The execution entry point is main().
    2) Consider adding some additional tests in doTestsPass().
    3) Implement findFirst(str) correctly.
    4) If time permits, some possible follow-ups. 
"""

"""
Finds the first character that does not repeat anywhere in the input string 
If all characters are repeated, return 0 
Given "apple", the answer is "a" 
Given "racecars", the answer is "e" 
Given "ababdc", the answer is "d" 
"""
def findFirst(input): 
    charFrequency = {}

    for c in input: 
        charFrequency[c] = charFrequency.get(c, 0) + 1. 
    for c in input: 
        if(charFrequency[c] == 1): 
            return c 
    return 0 
"""
Returns true if all tests pass, Otherwise returns false
"""
def doTestsPass(): 
    tests = {"racecar":'e', "apple":'a', "ababdc":'d', "xxyyzz":0 } 
    for test in tests.items(): 
        result = findFirst(test[0]) 
        if result != test[1]: 
            print("Test Failed: " + test[0] + " expected:" + test[1] + " actual: " + result + "\n") 
            return False 
    return True
if __name__ == "__main__":
    b=doTestsPass()
    print(b)


