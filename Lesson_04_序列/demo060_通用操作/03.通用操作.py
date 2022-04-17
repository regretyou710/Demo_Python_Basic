# + 和 *
# +可以將兩個列表拼接為一個列表
my_list = [1,2,3] + [4,5,6]

# * 可以將列表重複指定的次數
my_list = [1,2,3] * 5

# print(my_list)

# 創建一個列表
stus = ['孫悟空','豬八戒','沙和尚','唐僧','蜘蛛精','白骨精','沙和尚','沙和尚']

# in 和 not in
# in用來檢查指定元素是否存在於列表中
#   如果存在，返回True，否則返回False
# not in用來檢查指定元素是否不在列表中
#   如果不在，返回True，否則返回False
# print('牛魔王' not in stus)
# print('牛魔王' in stus)

# len()獲取列表中的元素的個數

# min() 獲取列表中的最小值
# max() 獲取列表中的最大值
arr = [10,1,2,5,100,77]
# print(min(arr) , max(arr))

# 兩個方法（method），方法和函數基本上是一樣，只不過方法必須通過 對象.方法() 的形式調用
# xxx.print() 方法實際上就是和對象關係緊密的函數
# s.index() 獲取指定元素在列表中的第一次出現時索引
# print(stus.index('沙和尚'))
# index()的第二個參數，表示查找的起始位置 ， 第三個參數，表示查找的結束位置
# print(stus.index('沙和尚',3,7))
# 如果要獲取列表中沒有的元素，會拋出異常
# print(stus.index('牛魔王')) ValueError: '牛魔王' is not in list
# s.count() 統計指定元素在列表中出現的次數
print(stus.count('牛魔王'))