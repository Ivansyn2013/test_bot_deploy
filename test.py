import os
from dotenv import load_dotenv


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

if __name__ == "__main__":
    print('__name__ == "__main__"')
    print(os.getenv('BOTTOKEN'))
else:
    print(print('__name__ =! "__main__"'))