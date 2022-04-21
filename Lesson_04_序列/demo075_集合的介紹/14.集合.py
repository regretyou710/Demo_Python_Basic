# 集合
# 使用 {} 來創建集合
s = {10,3,5,1,2,1,2,3,1,1,1,1} # <class 'set'>
# s = {[1,2,3],[4,6,7]} TypeError: unhashable type: 'list'
# 使用 set() 函數來創建集合
s = set() # 空集合
# 可以通過set()來將序列和字典轉換為集合
s = set([1,2,3,4,5,1,1,2,3,4,5])
s = set('hello')
s = set({'a':1,'b':2,'c':3}) # 使用set()將字典轉換為集合時，只會包含字典中的鍵

# 創建集合
s = {'a' , 'b' , 1 , 2 , 3 , 1}

# 使用in和not in來檢查集合中的元素
# print('c' in s)

# 使用len()來獲取集合中元素的數量
# print(len(s))

# add() 向集合中添加元素
s.add(10)
s.add(30)

# update() 將一個集合中的元素添加到當前集合中
#   update()可以傳遞序列或字典作為參數，字典只會使用鍵
s2 = set('hello')
s.update(s2)
s.update((10,20,30,40,50))
s.update({10:'ab',20:'bc',100:'cd',1000:'ef'})

# {1, 2, 3, 100, 40, 'o', 10, 1000, 'a', 'h', 'b', 'l', 20, 50, 'e', 30}
# pop()隨機刪除並返回一個集合中的元素
# result = s.pop()

# remove()刪除集合中的指定元素
s.remove(100)
s.remove(1000)

# clear()清空集合
s.clear()

# copy()對集合進行淺複製

# print(result)
print(s , type(s))