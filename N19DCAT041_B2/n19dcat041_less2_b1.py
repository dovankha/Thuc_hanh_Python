#ex: 1
from itertools import count


def convert_m_to_yd(minute: int) -> list:
    m = minute
    hour = minute // 60
    year = hour // (24*365)
    date = (hour % (24*365))//24
    list = [year, date]
    print('{} minutes is approximately {} years and {} days'.format(m, year, date))
    return list


#ex: 2
def break_int_to_list(my_integer: int) -> list:
    _list = [int(index) for index in str(my_integer)] # convert int -> string -> add to _list
    return _list


#ex: 3
def fibonacci(number: int) -> list:
    _list = [0, 1]
    i = 1
    while (i < number):
        i += 1
        x = _list[i-1] + _list[i-2]
        _list.append(x)
    return _list


#ex: 4
def factorial(number: int) -> list:
    _sum = 1
    for i in range(1, number+1):
        _sum *= i
    _list = [_sum]
    return _list


#ex: 5
def is_prime(number: int) -> None:
    if (number < 2):
        return False
    for i in range(2, number//2):
        if (number % i == 0):
            return False
    return True


#ex: 6
def count_o_e_d(number: int) -> dict:
    odd = 0
    even = 0
    while (number != 0):
        if ((number % 10) % 2 == 0):
            even += 1
        else:
            odd += 1
        number = number // 10
    dict = {"even": even, "odd": odd}
    return dict


#ex: 7
def is_palindrome(string: str) -> None:
    if (string[::-1] == string):
        return True
    return False


#ex: 8
def rotate(string: str, number) -> str:
    string = string.upper()
    string_output = ""
    for i in range(0, len(string)):
        if ((ord(string[i])+13)) > 90:
            string_output += chr(64+(ord(string[i])+number)-90)
        else:
            string_output += chr((ord(string[i])+number) % 90)
    return string_output


#ex: 9
def de_rotate(string: str, number):
    string = string.upper()
    string_output = ""
    for i in range(0, len(string)):
        if (ord(string[i])-13) < 65:
            string_output += (chr(91-(13-(ord(string[i])-65))))
        else:
            string_output += (chr((ord(string[i])-number)))
    return string_output


if __name__ == "__main__":
    print('Ex 1: ', convert_m_to_yd(600))
    print('Ex 2: ', break_int_to_list(1234567))
    print('Ex 3: ', fibonacci(30))
    print('Ex 4: ', factorial(5))
    print('Ex 5: ', is_prime(17))
    print('Ex 6: ', count_o_e_d(1234567))
    print('Ex 7: ', is_palindrome('abcdcba'))
    print('Ex 8: ', rotate('KhaDepTrai', 13))
    print('Ex 9: ', de_rotate('XUNQRCGENV', 13))
