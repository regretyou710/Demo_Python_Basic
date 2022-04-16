# 求100以內所有的奇數之和
# 獲取所有100以內數
# i = 0
# # 創建一個變量，用來保存結果
# result = 0
# while i < 100 :
#     i += 1
#     # 判斷i是否是奇數
#     if i % 2 != 0:
#         result += i

# print('result =',result)

# 獲取100以內所有的奇數
# i = 1
# while i < 100:
#     print(i)
#     i += 2

# 求100以內所有7的倍數之和，以及個數
i = 7 
# 創建一個變量，來保存結果
result = 0
# 創建一個計數器，用來記錄循環執行的次數
# 計數器就是一個變量，專門用來記錄次數的變量
count = 0
while i < 100:
    # 為計數器加1
    count += 1
    result += i
    i += 7    

print('總和為：',result,'總數量為:',count)