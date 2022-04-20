# 字典
# 使用 {} 來創建字典
d = {} # 創建了一個空字典

# 創建一個包含有數據的字典
# 語法：
#   {key:value,key:value,key:value}
#   字典的值可以是任意對象
#   字典的鍵可以是任意的不可變對象（int、str、bool、tuple ...），但是一般我們都會使用str
#       字典的鍵是不能重複的，如果出現重複的後邊的會替換到前邊的
# d = {'name':'孫悟空' , 'age':18 , 'gender':'男' , 'name':'sunwukong'}
d = {
'name':'孫悟空' , 
'age':18 , 
'gender':'男' , 
'name':'sunwukong'
}

# print(d , type(d))

# 需要根據鍵來獲取值
# print(d['name'],d['age'],d['gender'])

# 如果使用了字典中不存在的鍵，會報錯
# print(d['hello']) KeyError: 'hello'