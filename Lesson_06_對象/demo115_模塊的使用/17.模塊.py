# import m

# # 訪問模塊中的變量：模塊名.變量名
# # print(m.a , m.b)

# # m.test2()

# p = m.Person()

# print(p.name)

def test2():
    print('這是主模塊中的test2')


# 也可以只引入模塊中的部分內容
# 語法 from 模塊名 import 變量,變量....
# from m import Person
# from m import test
# from m import Person,test
# from m import * # 引入到模塊中所有內容，一般不會使用
# p1 = Person()
# print(p1)
# test()
# test2()

# 也可以為引入的變量使用別名
# 語法：from 模塊名 import 變量 as 別名
# from m import test2 as new_test2

# test2()
# new_test2()

from m import *
# print(_c)

# import xxx
# import xxx as yyy
# from xxx import yyy , zzz , fff
# from xxx import *
# from xxx import yyy as zz
    