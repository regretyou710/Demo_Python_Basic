# 遍歷列表，指的就是將列表中的所有元素取出來
# 創建列表
stus = ['孫悟空','豬八戒','沙和尚','唐僧','白骨精','蜘蛛精']

# 遍歷列表
# print(stus[0])
# print(stus[1])
# print(stus[2])
# print(stus[3])

# 通過while循環來遍歷列表
# i = 0
# while i < len(stus):
#     print(stus[i])
#     i += 1

# 通過for循環來遍歷列表
# 語法：
#   for 變量 in 序列 :
#       代碼塊
# for循環的代碼塊會執行多次，序列中有幾個元素就會執行幾次
#   沒執行一次就會將序列中的一個元素賦值給變量，
#   所以我們可以通過變量，來獲取列表中的元素

for s in stus :
    print(s)