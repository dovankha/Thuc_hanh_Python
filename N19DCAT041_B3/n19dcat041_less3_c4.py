def bind(_string: str) -> list:
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
        _list1.append(index1)
    return _list1


f = open("split_word.txt", "r")
_string = f.read()
_string = bind(_string)
_list = list(set(_string))
_dict = {}
for index1 in _list:
    count = 0
    for index2 in _string:
        if index1 == index2:
            count += 1
    _dict[index1] = count
_dict = sorted(_dict.items(), key=lambda x: x[1], reverse=True)
print("Top words most popular: ")
for index in range(0, 20):
    print(_dict[index])
