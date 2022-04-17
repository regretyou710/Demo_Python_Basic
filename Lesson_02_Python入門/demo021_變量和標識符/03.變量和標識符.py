# Python中使用變量，不需要聲明，直接為變量賦值即可
a = 10

# 不能使用沒有進行過賦值的變量
# 如果使用沒有賦值過的變量，會報錯 NameError: name 'b' is not defined
# print(b)

# Python是一個動態類型的語言，可以為變量賦任意類型的值，也可以任意修改變量的值
a = 'hello'

# print(a)

# 標識符
# 在Python中所有可以自主命名的內容都屬於標識符
# 比如：變量名、函數名、類名
# 標識符必須遵循標識符的規範
#   1.標識符中可以含有字母、數字、_，但是不能使用數字開頭
#       例子：a_1 _a1 _1a
#   2.標識符不能是Python中的關鍵字和保留字
#       也不建議使用Python中的函數名作為標識符,因為這樣會導致函數被覆蓋
#   3.命名規範：
#       在Python中註意遵循兩種命名規範：
#           下劃線命名法
#               所有字母小寫，單詞之間使用_分割
#               max_length min_length hello_world xxx_yyy_zzz
#           帕斯卡命名法（大駝峰命名法）  
#               首字母大寫，每個單詞開頭字母大寫，其餘字母小寫
#               MaxLength MinLength HelloWorld XxxYyyZzz  
#       
#   如果使用不符合標準的標識符，將會報錯 SyntaxError: invalid syntax    
#   練習：嘗試自己定義幾個變量（複雜一些，嘗試不同的命名法），然後打印一些變量
#           通過搜索引擎搜索還有哪些其他的命名規範
_b123 = 20
# print(_b123)

# print = 123
# print(print)