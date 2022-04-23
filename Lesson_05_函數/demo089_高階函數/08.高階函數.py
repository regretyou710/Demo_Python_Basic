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