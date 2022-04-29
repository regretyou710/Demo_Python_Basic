import os
from pprint import pprint

# os.listdir() 獲取指定目錄的目錄結構
# 需要一個路徑作為參數，會獲取到該路徑下的目錄結構，默認路徑為 . 當前目錄
# 該方法會返回一個列表，目錄中的每一個文件（夾）的名字都是列表中的一個元素
# r = os.listdir()
r = os.listdir('..')
    
# os.getcwd() 獲取當前所在的目錄
r = os.getcwd()

# os.chdir() 切換當前所在的目錄 作用相當於 cd
# os.chdir('c:/')

# r = os.getcwd()

# 創建目錄
# os.mkdir("aaa") # 在當前目錄下創建一個名字為 aaa 的目錄

# 刪除目錄
# os.rmdir('abc')

# open('aa.txt','w')
# 刪除文件
# os.remove('aa.txt')

# os.rename('舊名字','新名字') 可以對一個文件進行重命名，也可以用來移動一個文件
# os.rename('aa.txt','bb.txt')
os.rename('bb.txt','c:/users/lilichao/desktop/bb.txt')

pprint(r)