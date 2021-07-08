# Problem Name is Magic Potion PLEASE DO NOT REMOVE THIS LINE. 

"""
Instructions to candidate. 
1) Run this code in the REPL to observe its behaviour. The execution entry point is main. 
2) Consider adding some additional tests in do_tests_pass().
3) Implement minimal_steps() correctly. 
4) If time permits, some possible follow-ups. 


Question: Hermione is preparing a cheat-sheet for her final exam in Potions class. To create a potion, one must combine ingredients in a specific order, any of which may be repeated.


As an example, consider the following potion which uses 4 distinct ingredients (A,B,C,D) in 11 steps: A, 6, A, 6, C, A, 6, A, 6, C, D 
Hermione realizes she can save tremendous space on her cheat-sheet by introducing a special instruction, '*', which means "repeat from the beginning". 


Using these optimizations, Hermione is able to encode the potion above using only 6 characters: A,B,*,C,*,D 

Your job is to write a function that takes as input an un-encoded potion and returns the minimum number of characters required to encode the potion on Hermione's Cheat Sheet. 

"""

import sys 
# Function to return the minimal number of steps 
def minimal_steps( ingredients ): 
    n = len( ingredients ) 
    if n == 0: 
        return 0 
    dp = [ sys.maxsize ] * n 
    dp[0] = 1 
    for i in range(1, n):
        dp[ i ] = min(dp[ i ], dp[ i - 1 ] + 1) 
        
        # If the string can be replicated, we need to update at (2*i + 1)
        if ingredients[ 0: i + 1 ] == ingredients[ i + 1: 2*i + 2 ]:
            dp[ 2*i + 1 ] = dp[ i ] + 1 
    print(dp)
    return dp[ n - 1 ] 
    
"""
Returns true if all tests pass. Otherwise returns false. 
TODO: implement some tests. We've included a trivial boilerplate 
"""

def do_tests_pass(): 
    return (minimal_steps( "ABCDABCE" ) == 8 and minimal_steps( "ABCABCE" ) == 5 and 
            minimal_steps("AAAAAA") == 4 and minimal_steps("AAAABBBB") == 7 and 
            minimal_steps("ABABCABABCD") == 6 )
    
if __name__ == "__main__":
    result = do_tests_pass() 
    if result: 
        print( "All tests passed" ) 
    else: 
        print( "Tests failed" ) 

