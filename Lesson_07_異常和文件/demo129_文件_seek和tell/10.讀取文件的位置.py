# with open('demo.txt','rb') as file_obj:
#     # print(file_obj.read(100))
#     # print(file_obj.read(30))

#     # seek() 可以修改當前讀取的位置
#     file_obj.seek(55)
#     file_obj.seek(80,0)
#     file_obj.seek(70,1)
#     file_obj.seek(-10,2)
#     # seek()需要兩個參數
#     #   第一個 是要切換到的位置
#     #   第二個 計算位置方式
#     #       可選值：
#     #           0 從頭計算，默認值
#     #           1 從當前位置計算
#     #           2 從最後位置開始計算

#     print(file_obj.read())

#     # tell() 方法用來查看當前讀取的位置
#     print('當前讀取到了 -->',file_obj.tell())

with open('demo2.txt','rt' , encoding='utf-8') as file_obj:
    # print(file_obj.read(100))
    # print(file_obj.read(30))

    # seek() 可以修改當前讀取的位置
    file_obj.seek(9)
    # seek()需要兩個參數
    #   第一個 是要切換到的位置
    #   第二個 計算位置方式
    #       可選值：
    #           0 從頭計算，默認值
    #           1 從當前位置計算
    #           2 從最後位置開始計算

    print(file_obj.read())

    # tell() 方法用來查看當前讀取的位置
    print('當前讀取到了 -->',file_obj.tell())