# 創建字典
# 使用{}
# 語法：{k1:v1,k2:v2,k3:v3}

# 使用 dict()函數來創建字典
# 每一個參數都是一個鍵值對，參數名就是鍵，參數名就是值（這種方式創建的字典，key都是字符串）
d = dict(name='孫悟空',age=18,gender='男') 

# 也可以將一個包含有雙值子序列的序列轉換為字典
# 雙值序列，序列中只有兩個值，[1,2] ('a',3) 'ab'
# 子序列，如果序列中的元素也是序列，那麼我們就稱這個元素為子序列
# [(1,2),(3,5)]
d = dict([('name','孫悟飯'),('age',18)])
# print(d , type(d))
d = dict(name='孫悟空',age=18,gender='男') 

# len() 獲取字典中鍵值對的個數
# print(len(d))

# in 檢查字典中是否包含指定的鍵
# not in 檢查字典中是否不包含指定的鍵
# print('hello' in d)

# 獲取字典中的值，根據鍵來獲取值
# 語法：d[key]
# print(d['age'])

# n = 'name'
# print(d[n])

# 通過[]來獲取值時，如果鍵不存在，會拋出異常 KeyError
# get(key[, default]) 該方法用來根據鍵來獲取字典中的值
#   如果獲取的鍵在字典中不存在，會返回None
#   也可以指定一個默認值，來作為第二個參數，這樣獲取不到值時將會返回默認值
# print(d.get('name'))
# print(d.get('hello','默認值'))

# 修改字典
# d[key] = value 如果key存在則覆蓋，不存在則添加
d['name'] = 'sunwukong' # 修改字典的key-value
d['address'] = '花果山' # 向字典中添加key-value

# print(d)
# setdefault(key[, default]) 可以用來向字典中添加key-value
#   如果key已經存在於字典中，則返回key的值，不會對字典做任何操作
#   如果key不存在，則向字典中添加這個key，並設置value
result = d.setdefault('name','豬八戒')
result = d.setdefault('hello','豬八戒')

# print('result =',result)
# print(d)

# update([other])
# 將其他的字典中的key-value添加到當前字典中
# 如果有重複的key，則後邊的會替換到當前的
d = {'a':1,'b':2,'c':3}
d2 = {'d':4,'e':5,'f':6, 'a':7}
d.update(d2)

# print(d)
# 刪除，可以使用 del 來刪除字典中的 key-value
del d['a']
del d['b']

# popitem()
# 隨機刪除字典中的一個鍵值對，一般都會刪除最後一個鍵值對
#   刪除之後，它會將刪除的key-value作為返回值返回
#   返回的是一個元組，元組中有兩個元素，第一個元素是刪除的key，第二個是刪除的value
# 當使用popitem()刪除一個空字典時，會拋出異常 KeyError: 'popitem(): dictionary is empty'
# d.popitem()
# result = d.popitem()

# pop(key[, default])
# 根據key刪除字典中的key-value
# 會將被刪除的value返回！
# 如果刪除不存在的key，會拋出異常
#   如果指定了默認值，再刪除不存在的key時，不會報錯，而是直接返回默認值
result = d.pop('d')
result = d.pop('z','這是默認值')

# del d['z'] z不存在，報錯
# result = d.popitem()
# result = d.popitem()
# result = d.popitem()
# result = d.popitem()

# clear()用來清空字典
d.clear()

# print('result =',result)
# print(d)

# copy()
# 該方法用於對字典進行淺複製
# 複製以後的對象，和原對像是獨立，修改一個不會影響另一個
# 注意，淺複製會簡單複制對象內部的值，如果值也是一個可變對象，這個可變對像不會被複製
d = {'a':1,'b':2,'c':3}
d2 = d.copy()
# d['a'] = 100

d = {'a':{'name':'孫悟空','age':18},'b':2,'c':3}
d2 = d.copy()
d2['a']['name'] = '豬八戒'


print('d = ',d , id(d))
print('d2 = ',d2 , id(d2))