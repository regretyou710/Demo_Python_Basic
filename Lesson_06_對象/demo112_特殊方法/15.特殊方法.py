# 特殊方法，也稱為魔術方法
# 特殊方法都是使用__開頭和結尾的
# 特殊方法一般不需要我們手動調用，需要在一些特殊情況下自動執行

# 定義一個Person類
class Person(object):
    """人類"""
    def __init__(self, name , age):
        self.name = name
        self.age = age

    # __str__（）這個特殊方法會在嘗試將對象轉換為字符串的時候調用
    # 它的作用可以用來指定對象轉換為字符串的結果  （print函數）  
    def __str__(self):
        return 'Person [name=%s , age=%d]'%(self.name,self.age)        

    # __repr__()這個特殊方法會在對當前對象使用repr()函數時調用
    # 它的作用是指定對像在 ‘交互模式’中直接輸出的效果    
    def __repr__(self):
        return 'Hello'        

    # object.__add__(self, other)
    # object.__sub__(self, other)
    # object.__mul__(self, other)
    # object.__matmul__(self, other)
    # object.__truediv__(self, other)
    # object.__floordiv__(self, other)
    # object.__mod__(self, other)
    # object.__divmod__(self, other)
    # object.__pow__(self, other[, modulo])
    # object.__lshift__(self, other)
    # object.__rshift__(self, other)
    # object.__and__(self, other)
    # object.__xor__(self, other)
    # object.__or__(self, other)

    # object.__lt__(self, other) 小於 <
    # object.__le__(self, other) 小於等於 <=
    # object.__eq__(self, other) 等於 ==
    # object.__ne__(self, other) 不等於 !=
    # object.__gt__(self, other) 大於 >
    # object.__ge__(self, other) 大於等於 >= 
    
    # __len__()獲取對象的長度

    # object.__bool__(self)
    # 可以通過bool來指定對象轉換為布爾值的情況
    def __bool__(self):
        return self.age > 17

    # __gt__會在對像做大於比較的時候調用，該方法的返回值將會作為比較的結果
    # 他需要兩個參數，一個self表示當前對象，other表示和當前對像比較的對象
    # self > other
    def __gt__(self , other):
        return self.age > other.age


# 創建兩個Person類的實例        
p1 = Person('孫悟空',18)
p2 = Person('豬八戒',28)

# 打印p1
# 當我們打印一個對象時，實際上打印的是對象的中特殊方法 __str__()的返回值
# print(p1) # <__main__.Person object at 0x04E95090>
# print(p1)
# print(p2)

# print(repr(p1))

# t = 1,2,3
# print(t) # (1, 2, 3)

# print(p1 > p2)
# print(p2 > p1)

# print(bool(p1))

# if p1 :
#     print(p1.name,'已經成年了')
# else :
#     print(p1.name,'還未成年了')