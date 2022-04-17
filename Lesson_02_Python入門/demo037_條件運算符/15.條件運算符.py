# 條件運算符（三元運算符）
# 語法： 語句1 if 條件表達式 else 語句2
# 執行流程：
#   條件運算符在執行時，會先對條件表達式進行求值判斷
#       如果判斷結果為True，則執行語句1，並返回執行結果
#       如果判斷結果為False，則執行語句2，並返回執行結果
# 練習：
#   現在有a b c三個變量，三個變量中分別保存有三個數值，
#       請通過條件運算符獲取三個值中的最大值

# print('你好') if False else print('Hello')

a = 30
b = 50

# print('a的值比較大！') if a > b else print('b的值比較大！')
# 獲取a和b之間的較大值
max = a if a > b else b

print(max)