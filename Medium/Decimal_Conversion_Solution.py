# Problem Name is &&& Decimal Conversion &&& PLEASE DO NOT REMOVE THIS LINE.
# Instructions to candidate.
# 1) Run this code in the REPL to observe its behaviour. The execution entry point is __main__.
# 2) Consider adding some additional tests in doTestsPass().
# 3) If time permits, try to improve your implementation.


def vulgarToDecimal(numerator, denominator):
    if denominator == 0:
        return 'NaN'
    integer = str(int(numerator / denominator))
    rest = int(numerator) % denominator
    if rest == 0:
        return integer
    afterDot = ''
    numeratorToPos = dict()
    cyclePos = int(-1)
    while rest != 0:
        numerator = rest * 10
        if numerator in numeratorToPos:
            cyclePos = numeratorToPos[numerator] - 1
            break
        digit = str(int(numerator / denominator))
        afterDot += digit
        numeratorToPos[numerator] = len(afterDot)
        rest = numerator % denominator
    if cyclePos > -1:
        afterDot = afterDot[:cyclePos] + '(' + afterDot[cyclePos:] + ')'
    return integer + '.' + afterDot

def doTestsPass():
    testsPassed = True
    testsPassed &= vulgarToDecimal(1, 0) == 'NaN'
    testsPassed &= vulgarToDecimal(1, 2) == '0.5'
    testsPassed &= vulgarToDecimal(1, 3) == '0.(3)'

    if testsPassed:
        print('Tests passed')
        return 0
    print('Tests failed')
    return 1

if __name__ == '__main__':
    doTestsPass()

