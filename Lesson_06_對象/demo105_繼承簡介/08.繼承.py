# 繼承

# 定義一個類 Animal（動物）
#   這個類中需要兩個方法：run() sleep() 
class Animal:
    def run(self):
        print('動物會跑~~~')

    def sleep(self):
        print('動物睡覺~~~')

    # def bark(self):
    #     print('動物嚎叫~~~')   

# 定義一個類 Dog（狗）
#   這個類中需要三個方法：run() sleep() bark()
# class Dog:
#     def run(self):
#         print('狗會跑~~~')

#     def sleep(self):
#         print('狗睡覺~~~')

#     def bark(self):
#         print('汪汪汪~~~') 

# 有一個類，能夠實現我們需要的大部分功能，但是不能實現全部功能
# 如何能讓這個類來實現全部的功能呢？
#   ① 直接修改這個類，在這個類中添加我們需要的功能
#       - 修改起來會比較麻煩，並且會違反OCP原則
#   ② 直接創建一個新的類
#       - 創建一個新的類比較麻煩，並且需要大量的進行複制粘貼，會出現大量的重複性代碼
#   ③ 直接從Animal類中來繼承它的屬性和方法
#       - 繼承是面向對像三大特性之一
#       - 通過繼承我們可以使一個類獲取到其他類中的屬性和方法
#       - 在定義類時，可以在類名後的括號中指定當前類的父類（超類、基類、super）
#           子類（衍生類）可以直接繼承父類中的所有的屬性和方法
#           
#  通過繼承可以直接讓子類獲取到父類的方法或屬性，避免編寫重複性的代碼，並且也符合OCP原則
#   所以我們經常需要通過繼承來對一個類進行擴展

class Dog(Animal):
    def bark(self):
        print('汪汪汪~~~') 

    def run(self):
        print('狗跑~~~~')    

class Hashiqi(Dog):
    def fan_sha(self):
        print('我是一隻傻傻的哈士奇')        

d = Dog()
h = Hashiqi()

# d.run()
# d.sleep()
# d.bark()

# r = isinstance(d , Dog)
# r = isinstance(d , Animal)
# print(r)

# 在創建類時，如果省略了父類，則默認父類為object
#   object是所有類的父類，所有類都繼承自object
class Person(object):
    pass

# issubclass() 檢查一個類是否是另一個類的子類
# print(issubclass(Animal , Dog))
# print(issubclass(Animal , object))
# print(issubclass(Person , object))

# isinstance()用來檢查一個對像是否是一個類的實例
#   如果這個類是這個對象的父類，也會返回True
#   所有的對像都是object的實例
print(isinstance(print , object))