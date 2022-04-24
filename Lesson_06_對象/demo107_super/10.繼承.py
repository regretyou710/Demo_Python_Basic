class Animal:
    def __init__(self,name):
        self._name = name

    def run(self):
        print('動物會跑~~~')

    def sleep(self):
        print('動物睡覺~~~')

    @property
    def name(self):
        return self._name

    @name.setter    
    def name(self,name):
        self._name = name

# 父類中的所有方法都會被子類繼承，包括特殊方法，也可以重寫特殊方法
class Dog(Animal):

    def __init__(self,name,age):
        # 希望可以直接調用父類的__init__來初始化父類中定義的屬性
        # super() 可以用來獲取當前類的父類，
        #   並且通過super()返回對象調用父類方法時，不需要傳遞self
        # Animal.__init__(self,name)# 使用類名調用init時，需傳入self
        super().__init__(name)
        self._age = age

    def bark(self):
        print('汪汪汪~~~') 

    def run(self):
        print('狗跑~~~~')   

    @property
    def age(self):
        return self._age

    @age.setter    
    def age(self,age):
        self._age = age        

d = Dog('旺財',18) 

print(d.name)       
print(d.age)