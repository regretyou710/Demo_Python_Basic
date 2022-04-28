# open(file, mode='r', buffering=-1, encoding_=None, errors=None, newline=None, closefd=True, opener=None)
# 使用open函數來打開一個文件
# 參數：
#   file 要打開的文件的名字（路徑）
# 返回值：
#   返回一個對象，這個對象就代表了當前打開的文件

# 創建一個變量，來保存文件的名字
# 如果目標文件和當前文件在同一級目錄下，則直接使用文件名即可
# 先將目錄切換到 C:\Demo_Python_Basic\Lesson_07_異常和文件\demo122_文件_打開> 再執行04.打開文件.py
file_name = 'demo.txt'

# 在windows系統使用路徑時，可以使用/來代替 \
# 或者可以使用 \\ 來代替 \
# 或者也可以使用原始字符串
file_name = 'hello\\demo.txt'
file_name = r'hello\demo.txt'

# 表示路徑，可以使用..來返回一級目錄
file_name = '../hello/demo.txt'

# 如果目標文件距離當前文件比較遠，此時可以使用絕對路徑
# 絕對路徑應該從磁盤的根目錄開始書寫
#file_name = r'C:\Users\lilichao\Desktop\hello.txt'

file_obj = open(file_name) # 打開 file_name 對應的文件

print(file_obj)