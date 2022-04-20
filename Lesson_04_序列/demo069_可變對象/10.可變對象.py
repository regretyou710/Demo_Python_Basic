# # 可變對象
# a = [1,2,3]
# print('修改前：', a , id(a))

# # 通過索引修改列表
# a[0] = 10
# print('修改後：', a , id(a))

# # 為變量重新賦值
# a = [4,5,6]
# print('修改後：', a , id(a))


a = [1,2,3]
b = a
# b[0] = 10
b = [10,2,3]
# print("a",a,id(a))
# print("b",b,id(b))

# == !=  is is not
# == != 比較的是對象的值是否相等 
# is is not 比較的是對象的id是否相等（比較兩個對像是否是同一個對象）

a = [1,2,3]
b = [1,2,3]
print(a,b)
print(id(a),id(b))
print(a == b) # a和b的值相等，使用==會返回True
print(a is b) # a和b不是同一個對象，內存地址不同，使用is會返回False