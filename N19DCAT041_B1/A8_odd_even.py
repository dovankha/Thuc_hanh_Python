# NAME: DO VAN KHA 
# StudentID: N19DCAT041

def check_odd_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


number = int(input('Enter an integer number: '))
odd_number_count = 0
even_number_count = 0
while number != 0:
    temp = number % 10
    if check_odd_even(temp) == True:
        even_number_count += 1
    else:
        odd_number_count += 1
    number //= 10

print('The number of even numbers is {}'.format(even_number_count))
print('The number of odd numbers is {}'.format(odd_number_count))
