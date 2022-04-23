# 創建幾個函數

def add(a , b):
    '''
        求任意兩個數的和
    '''
    r = a + b
    return r


def mul(a , b):
    '''
        求任意兩個數的積
    '''
    r = a * b
    return r    

# 希望函數可以在計算前，打印開始計算，計算結束後打印計算完畢
#  我們可以直接通過修改函數中的代碼來完成這個需求，但是會產生以下一些問題
#   ① 如果要修改的函數過多，修改起來會比較麻煩
#   ② 並且不方便後期的維護
#   ③ 並且這樣做會違反開閉原則（OCP）
#           程序的設計，要求開發對程序的擴展，要關閉對程序的修改


# r = add(123,456)
# print(r)

# 我們希望在不修改原函數的情況下，來對函數進行擴展
def fn():
    print('我是fn函數....')

# 只需要根據現有的函數，來創建一個新的函數
def fn2():
    print('函數開始執行~~~')
    fn()
    print('函數執行結束~~~')

# fn2()    

def new_add(a,b):
    print('計算開始~~~')
    r = add(a,b)
    print('計算結束~~~')
    return r

# r = new_add(111,222)    
# print(r)

# 上邊的方式，已經可以在不修改源代碼的情況下對函數進行擴展了
#   但是，這種方式要求我們每擴展一個函數就要手動創建一個新的函數，實在是太麻煩了
#   為了解決這個問題，我們創建一個函數，讓這個函數可以自動的幫助我們生產函數

def begin_end(old):
    '''
        用來對其他函數進行擴展，使其他函數可以在執行前打印開始執行，執行後打印執行結束

        參數：
            old 要擴展的函數對象
    '''
    # 創建一個新函數
    def new_function(*args , **kwargs):
        print('開始執行~~~~')
        # 調用被擴展的函數
        result = old(*args , **kwargs)
        print('執行結束~~~~')
        # 返回函數的執行結果
        return result

    # 返回新函數        
    return new_function

f = begin_end(fn)
f2 = begin_end(add)
f3 = begin_end(mul)

# r = f()
# r = f2(123,456)
# r = f3(123,456)
# print(r)
# 向begin_end()這種函數我們就稱它為裝飾器
#   通過裝飾器，可以在不修改原來函數的情況下來對函數進行擴展
#   在開發中，我們都是通過裝飾器來擴展函數的功能的
# 在定義函數時，可以通過@裝飾器，來使用指定的裝飾器，來裝飾當前的函數
#   可以同時為一個函數指定多個裝飾器，這樣函數將會安裝從內向外的順序被裝飾 

def fn3(old):
    '''
        用來對其他函數進行擴展，使其他函數可以在執行前打印開始執行，執行後打印執行結束

        參數：
            old 要擴展的函數對象
    '''
    # 創建一個新函數
    def new_function(*args , **kwargs):
        print('fn3裝飾~開始執行~~~~')
        # 調用被擴展的函數
        result = old(*args , **kwargs)
        print('fn3裝飾~執行結束~~~~')
        # 返回函數的執行結果
        return result

    # 返回新函數        
    return new_function

@fn3
@begin_end
def say_hello():
    print('大家好~~~')

say_hello()