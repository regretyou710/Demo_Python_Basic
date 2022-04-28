file_name = 'demo2.txt'

try:
    # 調用open()來打開一個文件，可以將文件分成兩種類型
    # 一種，是純文本文件（使用utf-8等編碼編寫的文本文件）
    # 一種，是二進製文件（圖片、mp3、ppt等這些文件）
    # open()打開文件時，默認是以文本文件的形式打開的，但是open()默認的編碼為None
    #   所以處理文本文件時，必須要指定文件的編碼
    with open(file_name,encoding='utf-8') as file_obj:
        # 通過 read() 來讀取文件中的內容        
        content = file_obj.read()        
        print(content)
        
        
except FileNotFoundError :
    print(f'{file_name} 這個文件不存在！')