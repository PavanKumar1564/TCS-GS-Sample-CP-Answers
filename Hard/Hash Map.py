# Problem Name is &&& HashMap &&& PLEASE DO NOT REMOVE THIS LINE.
"""
/**
* Instructions to candidate. 
* 1) Run this code in the REPL to observe its behaviour. The execution entry point is main(). 
* 2) Consider adding some additional tests in doTestsPass(). 
* 3) Implement Myriashmap correctly.
* 4) If time permits, some possible follow-ups.
*/ 
/** 
* class MyHashMap
*
*Associates a key-value pair in memory such that lookups and inserts can be performed in 0(1) time for a reasonably 
* small set of data, and scales linearly (at worst) for larger sets of key-value pairs. 
* Each unique key is associated with one single value. */ 
"""
"""
"""
class Hashmap: 
    buckets = [] 
    def __init__(self):
        #poulate the buckets, start with an initial size of 10 
        for i in range(10): 
            self.buckets.append([]) 
    def put(self, key, val):
        hashIdx = hash(key) % len(self.buckets)
        bucket = self.buckets[hashIdx] 
        
        for i, b in enumerate(bucket): 
            if b[0] == key: 
                bucket[i] = (key, val) 
                return None 
        bucket.append((key, val)) 


    def get(self, key):
        hashIdx = hash(key) % len(self.buckets) 
        bucket = self.buckets[hashIdx] 
        
        for i, b in enumerate(bucket):
            if b[0] == key: 
                return b[1] 
        
    def get(self, key): 
        hashIdx = hash(key) % len(self.buckets)
        bucket = self.buckets[hashIdx] 
        
        for i, b in enumerate(bucket): 
            if b[0] == key: 
                return b[1] 
            
def doTestsPass(): 
    intList = [(1,2), (3,4), (5,6), (1,8)] 
    strList = [("one", "two"), ("three", "four"), ("one", "five")] 
    passed = True 
    intMap = Hashmap()
    for key, value in intList:
        intMap.put(key, value) 
        
        if intMap.get(key) != value: 
            passed = False 
            print("Test case failed [", key, ",", value, "]") 
    strMap = Hashmap() 
    for key, value in strList: 
        strMap.put(key, value) 
        
    if strMap.get(key) != value:
        passed = False
        print("Test case failed [", key, ",", value, "]") 
    if (passed): 
        print("All tests passed.") 
        
if __name__ == "__main__": 
    doTestsPass() 
