"""
Instructions to candidate. 
    1) Given a list of words, group them by anagrams 
    Input: ['cat', 'dog', 'god'] Output: [{'cat'}, {'dog', 'god'}] 
    2) Run this code in the REM_ to observe its behaviour. The execution entry point is main(). 
    3) Consider adding some additional tests in doTestsPass().
    4) If time permits, some possible follow-ups. 
"""

"""
Returns a list of sets of anagrams 

Args: 
    words - list of words to process 
    
Example:
    Input: ['cat', 'dog', 'god'] 
    Output: [{'cat'}, {'dog', 'god'}] 
"""
""" Returns True if all tests pass. Otherwise returns False. """
def group(words): 
    word_index = {}
    for word in words:
        word_key = "".join(sorted(list(word))) 
        word_index.setdefault(word_key, set()).add(word) 
    anagram_sets = list(word_index.values()) 
    return anagram_sets 

def doTestsPass(): 
     
    #TODO: add more test cases 
    words = ['cat', 'dog', 'cat', 'god'] 
    anagram_sets = [{'cat'}, {'dog', 'god'}] 
    result = group(words) 
    print("Result: {}".format(result)) 
    allTestsPass = True 
    for anagram_set in anagram_sets:
        if anagram_set not in result: 
            allTestsPass = False 
            print("Test Failed! Result missing anagram set: {}".format(anagram_set)) 
    if( allTestsPass ):
        print( "All tests pass." ) 
    else: 
            print( "There are test failures." ) 
    return( allTestsPass ) 
    
if __name__ == "__main__": 
    doTestsPass() 

