# 打開文件
file_name = 'demo.txt'

# 調用open()來打開文件
# file_obj = open(file_name)

# # 當我們獲取了文件對像以後，所有的對文件的操作都應該通過對象來進行
# # 讀取文件中的內容
# # read()方法，用來讀取文件中的內容，它會將內容全部保存為一個字符串返回
# content = file_obj.read()

# print(content)

# # 關閉文件
# # 調用close()方法來關閉文件
# file_obj.close()

# with ... as 語句
# with open(file_name) as file_obj :
#     # 在with語句中可以直接使用file_obj來做文件操作
#     # 此時這個文件只能在with中使用，一旦with結束則文件會自動close()
#     print(file_obj.read())


file_name = 'hello'

try:
    with open(file_name) as file_obj :
        print(file_obj.read())
except FileNotFoundError:
    print(f'{file_name} 文件不存在~~')