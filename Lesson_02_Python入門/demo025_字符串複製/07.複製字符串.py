# 創建一個變量來保存你的名字
name = '孫悟空'

# 使用四種方式來輸出，歡迎 xxx 光臨
# 拼串
print('歡迎 '+name+' 光臨！')
# 多個參數
print('歡迎',name,'光臨！')
# 佔位符
print('歡迎 %s 光臨！'%name)
# 格式化字符串
print(f'歡迎 {name} 光臨！')

# 字符串的複制（將字符串和數字相乘）
a = 'abc'
# * 在語言中表示乘法
# 如果將字符串和數字相乘，則解釋器會將字符串重複指定的次數並返回
a = a * 20

print(a)