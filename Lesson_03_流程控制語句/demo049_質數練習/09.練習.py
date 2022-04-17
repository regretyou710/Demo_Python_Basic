# 獲取用戶輸入的任意數，判斷其是否是質數。
num = int(input('輸入一個任意的大於1的整數：'))

# 判斷num是否是質數，只能被1和它自身整除的數就是質數
# 獲取到所有的可能整除num的整數
i = 2
# 創建一個變量，用來記錄num是否是質數，默認認為num是質數
flag = True
while i < num:
    # 判斷num能否被i整除
    # 如果num能被i整除，則說明num一定不是質數
    if num % i == 0 :
        # 一旦進入判斷，則證明num不是質數，則需要將flag修改為false
        flag = False
    i += 1

if flag :
    print(num,'是質數')
else :
    print(num,'不是質數')