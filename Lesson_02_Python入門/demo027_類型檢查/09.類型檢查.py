# 通過類型檢查，可以檢查只能值（變量）的類型

a = 123 # 數值
b = '123' # 字符串

# print('a =',a)
# print('b =',b)、

# type()用來檢查值的類型
# 該函數會將檢查的結果作為返回值返回，可以通過變量來接收函數的返回值
c = type('123')
c = type(a)
# print(type(b))
print(type(1)) # <class 'int'>
print(type(1.5)) # <class 'float'>
print(type(True)) # <class 'bool'>
print(type('hello'))  # <class 'str'>
print(type(None)) # <class 'NoneType'>