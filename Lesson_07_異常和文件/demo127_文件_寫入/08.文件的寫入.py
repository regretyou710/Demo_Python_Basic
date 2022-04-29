file_name = 'demo5.txt'

# 使用open()打開文件時必須要指定打開文件所要做的操作（讀、寫、追加）
# 如果不指定操作類型，則默認是 讀取文件 ， 而讀取文件時是不能向文件中寫入的
# r 表示只讀的
# w 表示是可寫的，使用w來寫入文件時，如果文件不存在會創建文件，如果文件存在則會截斷文件
#   截斷文件指刪除原來文件中的所有內容
# a 表示追加內容，如果文件不存在會創建文件，如果文件存在則會向文件中追加內容
# x 用來新建文件，如果文件不存在則創建，存在則報錯
# + 為操作符增加功能
#   r+ 即可讀又可寫，文件不存在會報錯
#   w+
#   a+
# with open(file_name , 'w' , encoding='utf-8') as file_obj:
# with open(file_name , 'r+' , encoding='utf-8') as file_obj:
with open(file_name , 'x' , encoding='utf-8') as file_obj:
    # write()來向文件中寫入內容，
    # 如果操作的是一個文本文件的話，則write()需要傳遞一個字符串作為參數
    # 該方法會可以分多次向文件中寫入內容
    # 寫入完成以後，該方法會返回寫入的字符的個數
    file_obj.write('aaa\n')
    file_obj.write('bbb\n')
    file_obj.write('ccc\n')
    r = file_obj.write(str(123)+'123123\n')
    r = file_obj.write('今天天氣真不錯')
    print(r)