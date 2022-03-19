import n19dcat041_less2_b1 as kha

while True:
    print('''
        +------------ MENU --------------+
        | 1: convert_m_to_yd()           |
        | 2: break_int_to_list()         |
        | 3: fibonacci()                 |
        | 4: factorial()                 |
        | 5: is_prime()	                 |
        | 6: count_o_e_d()               |
        | 7: is_palindrome()             |
        | 8: rotate()                    |
        | 9: de_rotate()                 |
        | 0: QUIT                        |
        +--------------------------------+
        ''')

    choice = int(input('Enter your choose: '))
    if choice == 1:
        minute = int(input('Enter minutes: '))
        print(kha.convert_m_to_yd(minute))
    elif choice == 2:
        integer = int(input('Enter an integer number: '))
        print(kha.break_int_to_list(integer))
    elif choice == 3:
        number = int(input("Enter length of Fibonacci: "))
        list = kha.fibonacci(number)
        print("The top ", number, " numbers of the Fibonacci sequence are:", end=" ")
        for i in list:
            print(i, end=" ")
    elif choice == 4:
        number = int(input("Enter a number number: "))
        list = kha.factorial(number)
        print("The factorial of {} is {}".format(number, list[0]))
    elif choice == 5:
        number = int(input("Enter an integer number: "))
        print(kha.is_prime(number))
    elif choice == 6:
        number = int(input("Enter an integer number: "))
        print(kha.count_o_e_d(number))
    elif choice == 7:
        x = input("Enter a string : ")
        print(kha.is_palindrome(x))
    elif choice == 8:
        x = input("Enter a string: ")
        y = int(input("Enter a key (only number): "))
        print(kha.rotate(x, y))
    elif choice == 9:
        x = input("Enter a string: ")
        y = int(input("Enter a key (only number): "))
        print(kha.de_rotate(x, y))
    elif choice == 0:
        print('GOOD BYE!')
        break
    else:
        print("Your choose is incorrect! Please choice again...")
