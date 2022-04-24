class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    # property裝飾器，用來將一個get方法，轉換為對象的屬性
    # 添加為property裝飾器以後，我們就可以像調用屬性一樣使用get方法
    # 使用property裝飾的方法，必須和屬性名是一樣的
    @property    
    def name(self):
        print('get方法執行了~~~')
        return self._name

    # setter方法的裝飾器：@屬性名.setter
    @name.setter    
    def name(self , name):
        print('setter方法調用了')
        self._name = name        

    @property
    def age(self):
        return self._age

    @age.setter    
    def age(self , age):
        self._age = age   

        

p = Person('豬八戒',18)

p.name = '孫悟空'
p.age = 28

print(p.name,p.age)