# range()是一個函數，可以用來生成一個自然數的序列
r = range(5) # 生成一個這樣的序列[0,1,2,3,4]
r = range(0,10,2)
r = range(10,0,-1)
# 該函數需要三個參數
#   1.起始位置（可以省略，默認是0）
#   2.結束位置
#   3.步長（可以省略，默認是1）

# print(list(r))

# 通過range()可以創建一個執行指定次數的for循環
# for()循環除了創建方式以外，其餘的都和while一樣，
#   包括else、包括break continue都可以在for循環中使用
#   並且for循環使用也更加簡單
# 將之前使用while循環做的練習，再使用for循環完成一次！
for i in range(30):
    print(i)

# for s in 'hello':
#     print(s)