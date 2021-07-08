# Problem Name is Run Length Encoding  PLEASE DO NOT REMOVE THIS LINE. 
"""
Instructions to candidate.
1) Run this code in the REPL to observe its behaviour. 
2) Consider adding some additional tests in doTestsPass(). 
3) Implement rle() correctly. 
4) If time permits, try to improve your implementation. 
Implement a run length encoding function. 

For a string input the function returns output encoded as follows: 
    
"a" -> "al" 
"aa" -> "a2" 
"aabbb" -> "a2b3" 
"aabbbaa" -> "a2b3a2" 
"""
def rle(testString):
    if(len(testString) == 0):
        return "" 
    lastseen = "" 
    result = "" 
    counter = 1 
    for let in testString:
        if( lastseen == let):
            counter += 1 
        else: 
            if lastseen != "":
                result = "%s%s%d" % (result, lastseen, counter)
            counter = 1 
            lastseen = let 
    result = "%s%s%d" % (result, lastseen, counter) 
    return result 
def Assert(actual,expected, message):
    if(actual == expected):
        print("PASSED: ", message, "Actual %s == Expected %s" % (actual, expected)); 

    else: 
        print("FAILED: ", message, "Actual %s != Expected %s" % (actual, expected)); 
        
def doTestsPass(): 
    Assert(rle(""),   "",    "Example 1"  );
    Assert(rle("a"),  "a1",  "Example 2"  );
    Assert(rle("aaa"), "a3",  "Example 3"  );
    Assert(rle("aaabbbaad"), "a3b3a2d1" ,  "Example 4" );
    
if __name__ == "__main__":
    doTestsPass() 

