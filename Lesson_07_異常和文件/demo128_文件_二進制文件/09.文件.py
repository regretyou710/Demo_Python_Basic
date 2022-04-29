file_name = 'C:\\Users\\WorkermanVM1\\Desktop\\aa.flac'

# 讀取模式
# t 讀取文本文件（默認值）
# b 讀取二進製文件

with open(file_name , 'rb') as file_obj:
    # 讀取文本文件時，size是以字符為單位的
    # 讀取二進製文件時，size是以字節為單位
    # print(file_obj.read(100))

    # 將讀取到的內容寫出來
    # 定義一個新的文件
    new_name = 'aa.flac'

    with open(new_name , 'wb') as new_obj:

        # 定義每次讀取的大小
        chunk = 1024 * 100

        while True :
            # 從已有的對像中讀取數據
            content = file_obj.read(chunk)

            # 內容讀取完畢，終止循環
            if not content :
                break

            # 將讀取到的數據寫入到新對像中
            new_obj.write(content)