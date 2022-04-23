# 比如有如下三行代碼，這三行代碼是一個完整的功能
# print('Hello')
# print('你好')
# print('再見')

# 定義一個函數
def fn() :
    print('這是我的第一個函數！')
    print('hello')
    print('今天天氣真不錯！')

# 打印fn
# print(fn) <function fn at 0x03D2B618>
# print(type(fn)) <class 'function'>

# fn是函數對象  fn()調用函數
# print是函數對象 print()調用函數
# fn()

# 定義一個函數，可以用來求任意兩個數的和
# def sum() :
#     a = 123
#     b = 456
#     print(a + b)

# sum()

# 定義函數時指定形參
def fn2(a , b) :
    # print('a =',a)
    # print('b =',b)
    print(a,"+",b,"=",a + b)

# 調用函數時，來傳遞實參
fn2(10,20)
fn2(123,456)