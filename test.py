import os
from dotenv import load_dotenv
from mimesis import Food
from mimesis import random
load_dotenv()

test1 = {'a':'1','b':'2','c':'3'}
test2 = {'a':'1','b':'2','c':'3','d':'4'}

myd = {'Банан спелый': 199, 'Белый лук': 149, 'Белый рис': 59, 'Белый сахар': 507, 'Белый шоколад': 503}
mid = 59

res = [x for x,y in myd.items() if y == mid]
print(res)
# print(dir(test1))
#
# dd = {x:test2[x] for x in test2 if x not in test1 }
#
#
#
#
# print(dd)

# test_dict = {name : id  for  name in zip([x for x in range(30)], Food.fruit()) for id in \
#         range(
#         30) }
frut = Food()

test_d = {x: id for x in range(100) for id in range(0,80)}
TEST_DICT = dict(sorted(test_d.items(), key=lambda x: x[1]))

print(TEST_DICT)
print('Len of test_dict ' + str(len(TEST_DICT)/14))
print('Len of test_dict ' + str(len(TEST_DICT)))

if __name__ == "__main__":
    print('__name__ == "__main__"')
    print(os.getenv('BOTTOKEN'))
else:
    print(print('__name__ =! "__main__"'))