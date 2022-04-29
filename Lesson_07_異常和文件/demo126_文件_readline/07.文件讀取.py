import pprint
import os
file_name = 'demo.txt'

with open(file_name , encoding='utf-8') as file_obj:
    # readline()
    # 該方法可以用來讀取一行內容
    # print(file_obj.readline(),end='')
    # print(file_obj.readline())
    # print(file_obj.readline())

    # readlines()
    # 該方法用於一行一行的讀取內容，它會一次性將讀取到的內容封裝到一個列表中返回
    # r = file_obj.readlines()
    # pprint.pprint(r[0])
    # pprint.pprint(r[1])
    # pprint.pprint(r[2])

    for t in file_obj:
        print(t)