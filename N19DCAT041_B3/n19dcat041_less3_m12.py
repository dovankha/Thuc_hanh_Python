import json
import math

f = open('data.json')

data = json.load(f)

st_code = input("Enter Student code: ")
_list = []
for i in data:
    if st_code == i["st_code"]:
        print("Name: ", i["last_name"] + " " + i["first_name"])
        _list = i["scores"]
        _max = 0
        avg_point = 0
        _min = 11
        for k in _list:
            avg_point = avg_point + k["score"]
            if k["score"] > _max:
                _max = k["score"]
            if k["score"] < _min:
                _min = k["score"]
        print("Max Score: ", int(_max * 10))
        print("Min Score: ", int(_min * 10))
        print("Average Score: ", int(round(avg_point / 4, 1) * 10))
        break
f.close()
