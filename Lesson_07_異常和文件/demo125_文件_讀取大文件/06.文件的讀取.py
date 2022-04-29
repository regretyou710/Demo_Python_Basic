file_name = 'demo2.txt'

try:
    # 調用open()來打開一個文件，可以將文件分成兩種類型
    # 一種，是純文本文件（使用utf-8等編碼編寫的文本文件）
    # 一種，是二進製文件（圖片、mp3、ppt等這些文件）
    # open()打開文件時，默認是以文本文件的形式打開的，但是open()默認的編碼為None
    #   所以處理文本文件時，必須要指定文件的編碼
    with open(file_name,encoding='utf-8') as file_obj:
        # 通過 read() 來讀取文件中的內容
        # 如果直接調用read()它會將文本文件的所有內容全部都讀取出來
        #   如果要讀取的文件較大的話，會一次性將文件的內容加載到內存中，容易導致內存洩漏
        #   所以對於較大的文件，不要直接調用read()
        # help(file_obj.read)
        # read()可以接收一個size作為參數，該參數用來指定要讀取的字符的數量
        #   默認值為-1，它會讀取文件中的所有字符
        #   可以為size指定一個值，這樣read()會讀取指定數量的字符，
        #       每一次讀取都是從上次讀取到位置開始讀取的
        #       如果字符的數量小於size，則會讀取剩餘所有的
        #       如果已經讀取到了文件的最後了，則會返回''空串
        # content = file_obj.read(-1)
        content = file_obj.read(6)
        content = file_obj.read(6)
        content = file_obj.read(6)
        content = file_obj.read(6)
        # print(content)
        # print(len(content))
except FileNotFoundError :
    print(f'{file_name} 這個文件不存在！')

# 讀取大文件的方式
file_name = 'demo.txt'

try:
    with open(file_name,encoding='utf-8') as file_obj:
        # 定義一個變量，來保存文件的內容
        file_content = ''
        # 定義一個變量，來指定每次讀取的大小
        chunk = 100
        # 創建一個循環來讀取文件內容
        while True:
            # 讀取chunk大小的內容
            content = file_obj.read(chunk)

            # 檢查是否讀取到了內容
            if not content:
                # 內容讀取完畢，退出循環
                break

            # 輸出內容
            # print(content,end='')
            file_content += content

except FileNotFoundError :
    print(f'{file_name} 這個文件不存在！')


print(file_content)