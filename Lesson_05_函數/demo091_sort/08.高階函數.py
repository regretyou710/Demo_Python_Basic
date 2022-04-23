# 高階函數
# 接收函數作為參數，或者將函數作為返回值的函數是高階函數
# 當我們使用一個函數作為參數時，實際上是將指定的代碼傳遞進了目標函數

# 創建一個列表
l = [1,2,3,4,5,6,7,8,9,10]

# 定義一個函數
#   可以將指定列表中的所有的偶數，保存到一個新的列表中返回

# 定義一個函數，用來檢查一個任意的數字是否是偶數
def fn2(i) :
    if i % 2 == 0 :
        return True

    return False    

# 這個函數用來檢查指定的數字是否大於5
def fn3(i):
    if i > 5 :
        return True    
    return False

def fn(func , lst) :

    '''
        fn()函數可以將指定列表中的所有偶數獲取出來，並保存到一個新列表中返回

        參數：
            lst：要進行篩選的列表
    '''
    # 創建一個新列表
    new_list = []

    # 對列表進行篩選
    for n in lst :
        # 判斷n的奇偶
        if func(n) :
            new_list.append(n)
        # if n > 5 :
        #     new_list.append(n)

            


    # 返回新列表
    return new_list

# def fn4(i):
#     if i % 3 == 0:
#         return True    
#     return False

def fn4(i):
    return i % 3 == 0
        
# print(fn(fn4 , l))

# filter()
# filter()可以從序列中過濾出符合條件的元素，保存到一個新的序列中
# 參數：
#  1.函數，根據該函數來過濾序列（可迭代的結構）
#  2.需要過濾的序列（可迭代的結構）
# 返回值：
#   過濾後的新序列（可迭代的結構）

# fn4是作為參數傳遞進filter()函數中
#   而fn4實際上只有一個作用，就是作為filter()的參數
#   filter()調用完畢以後，fn4就已經沒用
# 匿名函數 lambda 函數表達式 （語法糖）
#   lambda函數表達式專門用來創建一些簡單的函數，他是函數創建的又一種方式
#   語法：lambda 參數列表 : 返回值
#   匿名函數一般都是作為參數使用，其他地方一般不會使用

def fn5(a , b):
    return a + b

# (lambda a,b : a + b)(10,20)
# 也可以將匿名函數賦值給一個變量，一般不會這麼做
fn6 = lambda a,b : a + b
# print(fn6(10,30))


r = filter(lambda i : i > 5 , l)
# print(list(r))

# map()
# map()函數可以對可跌倒對像中的所有元素做指定的操作，然後將其添加到一個新的對像中返回
l = [1,2,3,4,5,6,7,8,9,10]

r = map(lambda i : i ** 2 , l)

# print(list(r))

# sort()
# 該方法用來對列表中的元素進行排序
# sort()方法默認是直接比較列表中的元素的大小
# 在sort()可以接收一個關鍵字參數 ， key
#   key需要一個函數作為參數，當設置了函數作為參數
#   每次都會以列表中的一個元素作為參數來調用函數，並且使用函數的返回值來比較元素的大小
l = ['bb','aaaa','c','ddddddddd','fff']
# l.sort(key=len)

l = [2,5,'1',3,'6','4']
l.sort(key=int)
# print(l)

# sorted()
# 這個函數和sort()的用法基本一致，但是sorted()可以對任意的序列進行排序
#   並且使用sorted()排序不會影響原來的對象，而是返回一個新對象

l = [2,5,'1',3,'6','4']
# l = "123765816742634781"

print('排序前:',l)
print(sorted(l,key=int))
print('排序後:',l)