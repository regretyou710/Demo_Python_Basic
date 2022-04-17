# 模塊，通過模塊可以對Python進行擴展
# 引入一個time模塊，來統計程序執行的時間
from time import *
# time()函數可以用來獲取當前的時間，返回的單位是秒
# 獲取程序開始的時間
# 優化前：
#   10000個數 12.298秒
#   100000個數 沒有結果
# 第一次優化
#   10000個數 1.577秒
#   100000個數 
    
begin = time()

i = 2
while i <= 100000:
    flag = True
    j = 2 
    while j < i:
        if i % j == 0:
            flag = False
            # 一旦進入判斷，則證明i一定不是質數，此時內層循環沒有繼續執行的必要
            # 使用break來退出內層的循環
            break
        j += 1
    if flag :
        # print(i)  
        pass
    i += 1

# 獲取程序結束的時間
end = time()

# 計算程序執行的時間
print("程序執行花費了：",end - begin , "秒")