# 開箱即用
# 為了實現開箱即用的思想，Python中為我們提供了一個模塊的標準庫
# 在這個標準庫中，有很多很強大的模塊我們可以直接使用，
#   並且標準庫會隨Python的安裝一同安裝
# sys模塊，它裡面提供了一些變量和函數，使我們可以獲取到Python解析器的信息
#   或者通過函數來操作Python解析器
# 引入sys模塊
import sys

# pprint 模塊它給我們提供了一個方法 pprint() 該方法可以用來對打印的數據做簡單的格式化
import pprint

# sys.argv
# 獲取執行代碼時，命令行中所包含的參數
# 該屬性是一個列表，列表中保存了當前命令的所有參數
# print(sys.argv)

# sys.modules
# 獲取當前程序中引入的所有模塊
# modules是一個字典，字典的key是模塊的名字，字典的value是模塊對象
# pprint.pprint(sys.modules)

# sys.path
# 他是一個列表，列表中保存的是模塊的搜索路徑
# ['C:\\Users\\lilichao\\Desktop\\resource\\course\\lesson_06\\code',
# 'C:\\dev\\python\\python36\\python36.zip',
# 'C:\\dev\\python\\python36\\DLLs',
# 'C:\\dev\\python\\python36\\lib',
# 'C:\\dev\\python\\python36',
# 'C:\\dev\\python\\python36\\lib\\site-packages']
# pprint.pprint(sys.path)

# sys.platform
# 表示當前Python運行的平台
# print(sys.platform)

# sys.exit()
# 函數用來退出程序
# sys.exit('程序出現異常，結束！')
# print('hello')

# os 模塊讓我們可以對操作系統進行訪問
import os

# os.environ
# 通過這個屬性可以獲取到系統的環境變量
# pprint.pprint(os.environ['path'])

# os.system()
# 可以用來執行操作系統的名字
# os.system('dir')
os.system('notepad')