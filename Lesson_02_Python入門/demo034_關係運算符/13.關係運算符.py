# 關係運算符
# 關係運算符用來比較兩個值之間的關係，總會返回一個布爾值
# 如果關係成立，返回True，否則返回False
# > 比較左側值是否大於右側值
# >= 比較左側的值是否大於或等於右側的值
# < 比較左側值是否小於右側值
# <= 比較左側的值是否小於或等於右側的值
# == 比較兩個對象的值是否相等
# != 比較兩個對象的值是否不相等
#   相等和不等比較的是對象的值，而不是id
# is 比較兩個對像是否是同一個對象，比較的是對象的id
# is not 比較兩個對像是否不是同一個對象，比較的是對象的id
result = 10 > 20 # False
result = 30 > 20 # True
result = 30 < 20 # False
result = 10 >= 10 # True

result = 2 > True # True
# result = 2 > '1' TypeError: '>' not supported between instances of 'int' and 'str'

# 0032 > 0031
result = '2' > '1' # True
result = '2' > '11' # True

# 在Python中可以對兩個字符串進行大於（等於）或小於（等於）的運算，
#   當對字符串進行比較時，實際上比較的是字符串的Unicode編碼
#   比較兩個字符串的Unicode編碼時，是逐位比較的
#   利用該特性可以對字符串按照字母順序進行排序，但是對於中文來說意義不是特別大
#   注意：如果不希望比較兩個字符串的Unicode編碼，則需要將其轉換為數字然後再比較
#   0061 > 0062
result = 'a' > 'b' # False
result = 'c' < 'd' # True
result = 'ab' > 'b' # False

# print(int('2') > int('11'))

result = 1 == 1 # True
result = 'hello' == 'hello' # True
result = 'abc' == 'bcd' # False
result = 'abc' != 'bcd' # True
result = 1 == True # True
result = 1 is True # False
result = 1 is not True # True
print('result =',result)
print(id(1),id(True))