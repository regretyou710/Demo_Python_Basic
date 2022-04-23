# 返回值，返回值就是函數執行以後返回的結果
# 可以通過 return 來指定函數的返回值
# 可以之間使用函數的返回值，也可以通過一個變量來接收函數的返回值

def sum(*nums):
    # 定義一個變量，來保存結果
    result = 0
    # 遍曆元組，並將元組中的數進行累加
    for n in nums :
        result += n
    print(result)

# sum(123,456,789)
 

# return 後邊跟什麼值，函數就會返回什麼值
# return 後邊可以跟任意的對象，返回值甚至可以是一個函數
def fn():
    # return 'Hello'
    # return [1,2,3]
    # return {'k':'v'}
    def fn2() :
        print('hello')

    return fn2 # 返回值也可以是一個函數

r = fn() # 這個函數的執行結果就是它的返回值
# r()
# print(fn())
# print(r)

# 如果僅僅寫一個return 或者 不寫return，則相當於return None 
def fn2() :
    a = 10
    return 

# 在函數中，return後的代碼都不會執行，return 一旦執行函數自動結束
def fn3():
    print('hello')
    return
    print('abc')

# r = fn3()
# print(r)

def fn4() :
    for i in range(5):
        if i == 3 :
            # break 用來退出當前循環
            # continue 用來跳過當次循環
            return # return 用來結束函數
        print(i)
    print('循環執行完畢！')

# fn4()

def sum(*nums):
    # 定義一個變量，來保存結果
    result = 0
    # 遍曆元組，並將元組中的數進行累加
    for n in nums :
        result += n
    return result

r = sum(123,456,789)

# print(r + 778)

def fn5():
    return 10

# fn5 和 fn5()的區別
print(fn5) # fn5是函數對象，打印fn5實際是在打印函數對象 <function fn5 at 0x05771BB8>
print(fn5()) # fn5()是在調用函數，打印fn5()實際上是在打印fn5()函數的返回值 10