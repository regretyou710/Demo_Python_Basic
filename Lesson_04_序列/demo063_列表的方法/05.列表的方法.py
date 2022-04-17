# 列表的方法
stus = ['孫悟空','豬八戒','沙和尚','唐僧']
# print('原列表：',stus)

# append() 
# 向列表的最後添加一個元素
# stus.append('唐僧')

# insert()
# 向列表的指定位置插入一個元素
# 參數：
#   1.要插入的位置
#   2.要插入的元素
# stus.insert(2,'唐僧')

# extend()
# 使用新的序列來擴展當前序列
# 需要一個序列作為參數，它會將該序列中的元素添加到當前列表中
# stus.extend(['唐僧','白骨精'])
# stus += ['唐僧','白骨精']

# clear()
# 清空序列
# stus.clear()

# pop()
# 根據索引刪除並返回被刪除的元素

# result = stus.pop(2) # 刪除索引為2的元素
# result = stus.pop() # 刪除最後一個
# print('result =',result)

# remove()
# 刪除指定值得元素，如果相同值得元素有多個，只會刪除第一個
# stus.remove('豬八戒')

# reverse()
# 用來反轉列表
# stus.reverse()

# sort()
# 用來對列表中的元素進行排序，默認是升序排列
# 如果需要降序排列，則需要傳遞一個reverse=True作為參數
my_list = list('asnbdnbasdabd')
my_list = [10,1,20,3,4,5,0,-2]

print('修改前',my_list)

my_list.sort(reverse=True)
print('修改後',my_list)
# print('修改後：',stus)