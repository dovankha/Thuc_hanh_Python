def print_word_more_n(path, lenght: int) -> None:
    _file = open(path)
    read_file = _file.read()
    _file.close()
    for x in read_file.split():
        if len(x) > lenght:
            print(x)


lenght = int(input('Enter length of word: '))

#path: I run it on Pycharm. If you run it on Vscode ... don't work =)
print_word_more_n(r"words.txt", lenght)
