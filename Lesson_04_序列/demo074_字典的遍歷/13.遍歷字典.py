# 遍歷字典
# keys() 該方法會返回字典的所有的key
#   該方法會返回一個序列，序列中保存有字典的所有的鍵
d = {'name':'孫悟空','age':18,'gender':'男'}

# 通過遍歷keys()來獲取所有的鍵
# for k in d.keys() :
#     print(k , d[k])

# values()
# 該方法會返回一個序列，序列中保存有字典的所有的值
# for v in d.values():
#     print(v)

# items()
# 該方法會返回字典中所有的項
# 它會返回一個序列，序列中包含有雙值子序列
# 雙值分別是，字典中的key和value
# print(d.items())
for k,v in d.items() :
    print(k , '=' , v)