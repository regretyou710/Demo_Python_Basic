# 元組 tuple
# 元組是一個不可變的序列
# 它的操作的方式基本上和列表是一致的
# 所以你在操作元組時，就把元組當成是一個不可變的列表就ok了
# 一般當我們希望數據不改變時，就使用元組，其餘情況都使用列表

# 創建元組
# 使用()來創建元組
my_tuple = () # 創建了一個空元組
# print(my_tuple,type(my_tuple)) # <class 'tuple'>

my_tuple = (1,2,3,4,5) # 創建了一個5個元素的元組
# 元組是不可變對象，不能嘗試為元組中的元素重新賦值
# my_tuple[3] = 10 TypeError: 'tuple' object does not support item assignment
# print(my_tuple[3])

# 當元組不是空元組時，括號可以省略
# 如果元組不是空元組，它裡邊至少要有一個,
my_tuple = 10,20,30,40
my_tuple = 40,
# print(my_tuple , type(my_tuple))

my_tuple = 10 , 20 , 30 , 40

# 元組的解包（解構）
# 解包指就是將元組當中每一個元素都賦值給一個變量
a,b,c,d = my_tuple

# print("a =",a)
# print("b =",b)
# print("c =",c)
# print("d =",d)

a = 100
b = 300
# print(a , b)

# 交互a 和 b的值，這時我們就可以利用元組的解包
a , b = b , a

# print(a , b)
my_tuple = 10 , 20 , 30 , 40


# 在對一個元組進行解包時，變量的數量必須和元組中的元素的數量一致
# 也可以在變量前邊添加一個*，這樣變量將會獲取元組中所有剩餘的元素
a , b , *c = my_tuple
a , *b , c = my_tuple
*a , b , c = my_tuple
a , b , *c = [1,2,3,4,5,6,7]
a , b , *c = 'hello world'
# 不能同時出現兩個或以上的*變量
# *a , *b , c = my_tuple SyntaxError: two starred expressions in assignment
print('a =',a)
print('b =',b)
print('c =',c)