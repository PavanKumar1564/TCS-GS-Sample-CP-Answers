# Problem Name is &&& Longest Uniform Substring &&& PLEASE DO NOT REMOVE THIS LINE. 
"""
Instructions to candidate.
1) Run this code in the REPL to observe its behaviour. The execution entry point is specified at the bottom.
2) Your task is to implement the following function ('longest_uniform_substring). 
This function should return a tuple that correctly identifies the location of the longest uniform substring within the input string. 
e.g. - for the input: "abbbccda" the longest uniform substring is "bbb" (which starts at index 1 and is 3 characters long). - the tuple returned from the function call would be (1, 3) 3) If time permits, try to improve your implementation and add more test cases.
"""
def longest_uniform_substring(input):
    #todo: implement this function return (-1, 0)
    longest_start = -1
    longest = 0
    ix = 1
    length = len(input)
    while ix < length:
        start = ix - 1
        current_length = 1
        while ix < length and input[ix] == input[ix - 1]:
            ix += 1
            current_length += 1
        if current_length > longest:
            longest_start = start
            longest = current_length
        ix += 1
    return (longest_start, longest)

def do_tests_pass():
    """Returns True if the test passes. Otherwise returns False.""" 
    # todo: implement more tests
    test_cases = { 
                    "" : (-1, 0 ),
                    "10000111": (1, 4),
                    "aabbbbbCdAA": (2, 5)
                 }
    passed = True
    for input, result in test_cases.items():
        start, length = longest_uniform_substring(input)
        passed = passed and start == result[0] and length == result[1] 
    return passed

if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass!")
    else:
        print("At least one failure!") 