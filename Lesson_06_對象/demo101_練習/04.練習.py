class Dog:
    '''
        表示狗的類
    '''
    def __init__(self , name , age , gender , height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def jiao(self):
        '''
            狗叫的方法
        '''
        print('汪汪汪~~~')

    def yao(self):
        '''
            狗咬的方法
        '''  
        print('我咬你~~')

    def run(self):
        print('%s 快樂的奔跑著~~'%self.name)     


d = Dog('小黑',8,'male',30)

# 目前我們可以直接通過 對象.屬性 的方式來修改屬性的值，這種方式導致對像中的屬性可以隨意修改
#   非常的不安全，值可以任意修改，不論對錯
# 現在我們就需要一種方式來增強數據的安全性
#   1.屬性不能隨意修改（我讓你改你才能改，不讓你改你就不能改）
#   2.屬性不能修改為任意的值（年齡不能是負數）
d.name = '阿黃'
d.age = -10
d.run()

print(d.age)

# print(d.name , d.age , d.gender , d.height)