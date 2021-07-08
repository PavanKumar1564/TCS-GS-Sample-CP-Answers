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
    def __init__(self, entries):
        self.entries = entries
    def contains(self, word):
        return word in self.entries 
    def longestWord(self,letters, dictionary):
        d=dict()
        for i in dictionary.entries:
            flag=0
            for j in i:
                if j not in letters:
                    flag=1
                    break
            if flag==0:
                if(len(i) in d):
                    d[len(i)].append(i)
                else:
                    d[len(i)]=[i]
        m=sorted(d)[-1]
        return d[m]
        
words = ('to', 'toe', 'toes', 'doe', 'dog', 'god', 'dogs', 'book', 'banana')
dictionary = Dictionary(words) 

def doTestsPass():
    result = ['toe'] == dictionary.longestWord('toe', dictionary) 
    result = result and {'toes','dogs'} == set(dictionary.longestWord('losetdg', dictionary)) 
    if(result):
        print('All tests pass')
    else:
        print('There are test failures') 

if __name__ == "__main__":
    doTestsPass() 
