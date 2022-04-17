# 求100以內所有的質數
# 創建一個循環，求1-100以內所有的數
i = 2
while i <= 100:
    
    # 創建一個變量，記錄i的狀態，默認認為i是質數
    flag = True

    # 判斷i是否是質數
    # 獲取所有可能成為i的因數的數
    j = 2 
    while j < i:
        # 判斷i能否被j整除
        if i % j == 0:
            # i能被j整除，證明i不是質數，修改flag為False
            flag = False
        j += 1
    # 驗證結果並輸出
    if flag :
        print(i)   

    i += 1