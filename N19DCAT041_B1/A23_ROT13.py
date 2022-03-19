# NAME: DO VAN KHA
# StudentID: N19DCAT041

import sys
import string

str = string.ascii_letters
str_out = ''


def ROT13(str_input: string, key: int) -> None:
    global str_out  # khai bao la bien toan cuc de khi chay khong bi loi
    # Ma loi: "UnboundLocalError: local variable referenced before assignment"
    for char in str_input:
        # 52: tại vì 24 upper_letter + 24 lower_letter
        str_out += str[(str.find(char)+key) % 52]
    return str_out


program_name = sys.argv[0]
arguments = sys.argv[1:]
if len(arguments) > 2:  # Lon hon 2 vi <py name.py(vi tri 0) argv1(vi tri 1) agrv2(vi tri 2)]
    # argument[2] la string. Ep kieu -> int.
    print('String ROT13: ', ROT13(sys.argv[1], int(sys.argv[2])))
else:
    for index, char in enumerate(string.ascii_letters):
        print(index, '-', char, end='; ')

    str_input = input('Enter a string: ')
    key = int(input('Enter a key (integer): '))
    print('String ROT13: ', ROT13(str_input, key))
