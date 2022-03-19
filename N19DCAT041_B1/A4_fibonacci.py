# NAME: DO VAN KHA 
# StudentID: N19DCAT041

def fibonacci(n: int) -> int:
    """Return the 'n'th Fibonacci number, for possible 'n'."""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0
    result = None
    for index in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    return result


list = []
number = int(input('Enter an integer number: '))
for x in range(number):
    temp = fibonacci(x)
    list.append(temp)
print('The first {} numbers of the Fibonacci sequence are: {}'.format(number, list))
