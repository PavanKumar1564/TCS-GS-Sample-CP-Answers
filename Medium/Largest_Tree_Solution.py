"""
** Instructions:
** Given a forest ( one or more disconnected trees ), find the root of largest tree
** and return its Id. If there are multiple such roots, return the smallest Id of them. 
**
** Complete the largestTree function in the editor below.
** It has one parameter, immediateParent, which is a map containing key-value pair indicating
** child -> parent relationship. The key is child and value is the corresponding
** immediate parent.
** Constraints
**      - Child cannot have more than one immediate parent.
**      - Parent can have more than one immediate child.
**      - The given key-value pair forms a well-formed forest ( a tree of n nodes will have n-1 edges )
** Example:
** 
** Input: 
** { { 1 -> 2 }, {3 -> 4} } 
** 
** Expected output: 2
** Explanation: There are two trees one having root of Id 2 and another having root of Id 4.
** Both trees have size 2. The smaller number of 2 and 4 is 2. Hence the answer is 2.
"""

"""Find the largest tree. """ 
def getTreeSize(parentToChild, rootlndex):
    result = 0
    stack = []
    stack. append(rootlndex)
    while(len(stack)>0):
        index = stack.pop()
        result = result + 1
        if index in parentToChild:
            for childIndex in parentToChild[index]:
                stack.append(childIndex) 
    return result 
""" Find the largest tree. """
def largestTree(immediateParent):
    maxTreeSize = 0
    minRootld = 0
    rootIndexes = []
    parentToChild = dict()
    for childlndex, parentIndex in immediateParent.items():
        parentToChild.setdefault(parentIndex, []).append(childlndex)
        if not parentIndex in immediateParent:
            rootIndexes.append(parentIndex) 
            for rootlndex in rootIndexes:
                treeSize = getTreeSize(parentToChild, rootlndex)
                if treeSize > maxTreeSize:
                    maxTreeSize = treeSize
                    minRootld = rootlndex
                elif treeSize == maxTreeSize:
                    minRootld = min (minRootld, rootlndex) 
    return minRootld 

def doTestsPass():
    """ Returns true if the tests pass. Otherwise, returns false """ 
    testCases = [
    # example
    (dict({1:2, 3:4}), 2), 
    # More than two trees
    (dict({2:3, 7:8, 12:15, 3:1, 13:15, 11:15, 9:8, 5:12}), 15), 
    # really large index values
    (dict({ 200000000:300000000, 500000000:200000000, 700000000:300000000, 600000000:700000000, 900000000:400000000, 100000000:400000000, 800000000:400000000, 1000000000:400000000}), 300000000), 
    # two trees of same size
    (dict({ 9:4, 1:4, 5:2, 8:4, 7:3, 2:3, 6:7, 10:4 }),3), 
    # tree sizes differ by one
    (dict({35:33, 33:28, 31:22, 28:25, 34:31, 29:27, 21:23, 25:21, 22:29}),23), ]
    
    passed = True
    for tc, expected in testCases:
        actual = largestTree(tc)
        if actual != expected:
            passed = False
            print("Failed for case ", tc, "\n expected ", expected, ", actual ", actual) 
    return passed 
if __name__ == "__main__": 
    result = doTestsPass() 
    if result:
        print("All tests pass\n")
    else:
        print("Tests fail\n");
