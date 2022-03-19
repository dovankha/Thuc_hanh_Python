# NAME: DO VAN KHA 
# StudentID: N19DCAT041

import sys


def gcd(x, y):
    while x*y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    return x + y


program_name = sys.argv[0]
arguments = sys.argv[1:]
print(program_name)
if len(arguments) > 2:
    n1, n2 = int(sys.argv[1]), int(sys.argv[2])
    print('gcd({},{}): {}'.format(n1, n2, gcd(n1, n2)))
else:
    n1 = int(input('Please enter number a: '))
    n2 = int(input('Please enter number b: '))
    print('gcd({},{}): {}'.format(n1, n2, gcd(n1, n2)))
