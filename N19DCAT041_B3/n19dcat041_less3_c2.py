def bind(_string):
    _list = list(_string.split())
    _list1 = []
    for index1 in _list:
        index1 = index1.lower()
        for index2 in range(0, len(index1)):
            if (ord(index1[index2]) >= 97 and ord(index1[index2]) <= 122) or (ord(index1[index2]) >= 48 and ord(index1[index2]) <= 57):
                pass
            else:
                index1 = index1.strip(index1[index2])
                break
        print(index1)
        _list1.append(index1)
        f = open('split_word.txt', 'a')
        f.write(index1 + '\n')
    return _list1


f = open("non_split_word.txt", "r")
_string = f.read()
print(bind(_string))
print("Done!")
