lst = [{'id': 33, 'Code': '392', 'Ccy': 'JPY'},
       {'id': 6, 'Code': '944', 'Ccy': 'AZN'},
       {'id': 7, 'Code': '050', 'Ccy': 'BDT'},
       {'id': 8, 'Code': '975', 'Ccy': 'BGN'},
       {'id': 9, 'Code': '048', 'Ccy': 'BHD'},
       {'id': 10, 'Code': '096', 'Ccy': 'BND'},
       {'id': 11, 'Code': '986', 'Ccy': 'BRL'},
       {'id': 12, 'Code': '933', 'Ccy': 'BYN', }
       ]

key = []
value = []
for i in lst:
    a = key.append(i["id"])
    b = value.append(i["Code"])
print(key)
print(value)
res = dict(zip(key, value))
print(res)
# >>> a = [1, 2, 3]
# >>> c = dict.fromkeys(a)
# >>> c
# {1: None, 2: None, 3: None}
# >>> d = dict.fromkeys(a, 10)
# >>> d
# {1: 10, 2: 10, 3: 10}

a = ['a', 'b', 'c', 'd']
b = [1, 2, 3, 4]
print(dict(zip(a, b)))