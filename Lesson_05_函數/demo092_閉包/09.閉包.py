# 將函數作為返回值返回，也是一種高階函數
# 這種高階函數我們也稱為叫做閉包，通過閉包可以創建一些只有當前函數能訪問的變量
#   可以將一些私有的數據藏到的閉包中

def fn():

    a = 10

    # 函數內部再定義一個函數
    def inner():
        print('我是fn2' , a)

    # 將內部函數 inner作為返回值返回   
    return inner

# r是一個函數，是調用fn()後返回的函數
# 這個函數實在fn()內部定義，並不是全局函數
# 所以這個函數總是能訪問到fn()函數內的變量
r = fn()    

# r()

# 求多個數的平均值
# nums = [50,30,20,10,77]

# sum()用來求一個列表中所有元素的和
# print(sum(nums)/len(nums))

# 形成閉包的要件
#   ① 函數嵌套
#   ② 將內部函數作為返回值返回
#   ③ 內部函數必須要使用到外部函數的變量
def make_averager():
    # 創建一個列表，用來保存數值
    nums = []

    # 創建一個函數，用來計算平均值
    def averager(n) :
        # 將n添加到列表中
        nums.append(n)
        # 求平均值
        return sum(nums)/len(nums)

    return averager

averager = make_averager()

print(averager(10))
print(averager(20))
print(averager(30))
print(averager(40))