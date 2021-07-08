# Problem Name is &&& Decimal Conversion &&& PLEASE DO NOT REMOVE THIS LINE.
# Instructions to candidate.
# 1) Run this code in the REPL to observe its behaviour. The execution entry point is __main__.
# 2) Consider adding some additional tests in doTestsPass().
# 3) If time permits, try to improve your implementation.


def vulgarToDecimal(numerator, denominator):
    if denominator==0:
        return 'NaN'
    if numerator==0:
        return "0"
    decim=numerator//denominator
    res = ""
    res += str(decim)
    if numerator%denominator==0:
        return res
    res+="."
    rem=numerator%denominator
    a={}
    idx=0
    flag=False
    while(rem>0 and not flag):
        if(rem in a):
            idx=a[rem]
            flag=True
            break
        else:
            a[rem]=len(res)
        rem=rem*10
        temp=rem//denominator
        res+=str(temp)
        rem=rem%denominator
    if flag==True:
        res+=")"
        x=res[:idx]
        x+="("
        x+=res[idx:]
        res=x
    
    return res


# Implement the method that provided numerator and denominator will return a string representing fraction's decimal form.
# Some fractions in decimal form have cyclic decimal points.
#
# Examples:
# 1/2 = 0.5
# 1/3 = 0.(3)

def doTestsPass():
    
    testsPassed = True
    testsPassed &= vulgarToDecimal(1, 0) == 'NaN'
    testsPassed &= vulgarToDecimal(1, 2) == '0.5'
    testsPassed &= vulgarToDecimal(1, 3) == '0.(3)'
    testsPassed &= vulgarToDecimal(8, 6) == '1.(3)'
    if testsPassed:
        print('Tests passed')
        return 0
    print('Tests failed')
    return 1


# doTestsPass()
# Returns 0 if all tests pass. Otherwise 1
#
# Consider adding more tests.

if __name__ == '__main__':
    doTestsPass()
