class Rectangle:
    '''
        表示矩形的類
    '''
    def __init__(self,width,height):
        self.hidden_width = width
        self.hidden_height = height

    def get_width(self):
        return self.hidden_width

    def get_height(self):
        return self.hidden_height   

    def set_width(self , width):
        self.hidden_width = width 

    def set_height(self , height):
        self.hidden_height = height 

    def get_area(self):
        return self.hidden_width * self.hidden_height        

# r = Rectangle(5,2)  
# r.set_width(10)
# r.set_height(20)

# print(r.get_area())     
 
 
# 可以為對象的屬性使用雙下劃線開頭，__xxx
# 雙下劃線開頭的屬性，是對象的隱藏屬性，隱藏屬性只能在類的內部訪問，無法通過對象訪問
# 其實隱藏屬性只不過是Python自動為屬性改了一個名字
#   實際上是將名字修改為了，_類名__屬性名 比如 __name -> _Person__name
# class Person:
#     def __init__(self,name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

#     def set_name(self , name):
#         self.__name = name        

# p = Person('孫悟空')

# print(p.__name) __開頭的屬性是隱藏屬性，無法通過對象訪問
# p.__name = '豬八戒'
# print(p._Person__name)
# p._Person__name = '豬八戒'

# print(p.get_name())

# 使用__開頭的屬性，實際上依然可以在外部訪問，所以這種方式我們一般不用
#   一般我們會將一些私有屬性（不希望被外部訪問的屬性）以_開頭
#   一般情況下，使用_開頭的屬性都是私有屬性，沒有特殊需要不要修改私有屬性
class Person:
    def __init__(self,name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self , name):
        self._name = name   

p = Person('孫悟空')

print(p._name)