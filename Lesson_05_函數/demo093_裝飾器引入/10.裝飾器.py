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