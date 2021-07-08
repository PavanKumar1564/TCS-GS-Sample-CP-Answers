# Problem Name is &&& Longest Word &&& PLEASE DO NOT REMOVE THIS LINE. 
"""
Instructions to candidate.
1) Given a a string of letters and a dictionary, the function longestWord should
    find the longest word or words in the dictionary that can be made from the letters
    Input: letters = "oet", dictionary = {"to","toe","toes"}
    Output: {"toe"} 
    Only lowercase letters will occur in the dictionary and the letters.
    The length of letters will be between 1 and 10 characters.
    The solution should work well for a dictionary of over 100,000 words
2) Run this code in the REPL to observe its behaviour. The execution entry point is main.
3) Consider adding some additional tests in doTestsPass(). 
4) Implement the longestWord() method correctly.
5) If time permits, introduce '?' which can represent any letter. "to?" could match to "toe", "ton" etc """

class Dictionary:
    # Pre-process dictionary so we have list of dictionary entries stored against a sorted string
    # e.g. "dgo"-> {"dog", "god")
    
    def __init__(self, entries):
        self.sortedLetters2Words = {}
        for word in entries:
            sortedLetters = "".join(sorted(word))
            self.sortedLetters2Words.setdefault(sortedLetters, [])
            self.sortedLetters2Words[sortedLetters].append(word) 
    def getEntriesForSortedLetters(self, sortedLetters):
        return self.sortedLetters2Words.get(sortedLetters, None); 
        
# For each string in set return a new set with all possibilities with 1 char dropped from lettersCombinations

def combinationsDroppingOneLetter(letterCombinations):
    oneLetterLessSet = set()
    for letters in letterCombinations:
        if (len(letters) > 1):
            for i in range(len(letters)):
                oneLetterLessSet.add(letters[0:i] + letters[i+1:])
    return oneLetterLessSet 
    
def longestWord(letters, dictionary):
    # To support ? wild card could expand all possibilites here. A better solution would be Tree/Trie based
    # Set with one entry of letters sorted
    considerLettersSet = {"".join(sorted(letters))}
    while len(considerLettersSet) > 0:
        #Get list of words in dictionary that match any of the set of sorted letters
        allFoundInDict = [dictionary.getEntriesForSortedLetters(item)for item in considerLettersSet]
        allFoundInDict = [word for sublist in allFoundInDict if sublist for word in sublist]
        if (len(allFoundInDict)>0):
            return allFoundInDict
        # Next time round loop will consider combinations of sorted letters with one less character
        considerLettersSet = combinationsDroppingOneLetter(considerLettersSet)
    return [] 
        
words = ('to', 'toe', 'toes', 'doe', 'dog', 'god', 'dogs', 'book', 'banana')
dictionary = Dictionary(words) 

def doTestsPass():
    result = {'ab', 'bc', 'ac'} == combinationsDroppingOneLetter({'abc'})
    result = result and {'ab', 'bb'} == combinationsDroppingOneLetter({'abb'})
    result = result and {'a', 'b'} == combinationsDroppingOneLetter({'ab','bb'})
    result = result and set() == combinationsDroppingOneLetter({'a','b'})
    result = result and set() == combinationsDroppingOneLetter({})
    result = result and ['toe'] == longestWord('toe', dictionary)
    result = result and {'toes','dogs'} == set(longestWord('osetdg', dictionary))
    result = result and {"doe",'toe','dog','god'} == set(longestWord('oetdg', dictionary))
    result = result and ['book'] == longestWord('obokt', dictionary)
    result = result and ['banana'] == longestWord('nanabaook', dictionary)
    result = result and [] == longestWord('a', dictionary) 
    
    
    if(result):
        print('All tests pass')
    else:
        print('There are test failures') 

if __name__ == "__main__":
    doTestsPass() 
