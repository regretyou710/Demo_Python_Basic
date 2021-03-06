# 格式化字符串
a = 'hello'

# 字符串之間也可以進行加法運算
# 如果將兩個字符串進行相加，則會自動將兩個字符串拼接為一個
a = 'abc' + 'haha' + '哈哈'
# a = 123 
# 字符串只能不能和其他的類型進行加法運算，如果做了會出現異常 TypeError: must be str, not int
# print("a = "+a) # 這種寫法在Python中不常見
a = 123
# print('a =',a)

# 在創建字符串時，可以在字符串中指定佔位符
# %s 在字符串中表示任意字符
# %f 浮點數佔位符
# %d 整數佔位符
b = 'Hello %s'%'孫悟空'
b = 'hello %s 你好 %s'%('tom','孫悟空')
b = 'hello %3.5s'%'abcdefg' # %3.5s字符串的長度限制在3-5之間
b = 'hello %s'%123.456
b = 'hello %.2f'%123.456
b = 'hello %d'%123.95
b = '呵呵'

# print('a = %s'%a)

# 格式化字符串，可以通過在字符串前添加一個f來創建一個格式化字符串
# 在格式化字符串中可以直接嵌入變量
c = f'hello {a} {b}'

print(f'a = {a}')

# 練習 創建一個變量保存你的名字，然後通過四種格式化字符串的方式
#   在命令行中顯示，歡迎 xxx 光臨！