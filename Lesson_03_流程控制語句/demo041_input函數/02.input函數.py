import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# input()函數
# 該函數用來獲取用戶的輸入
# input()調用後，程序會立即暫停，等待用戶輸入
#   用戶輸入完內容以後，點擊回車程序才會繼續向下執行
#   用戶輸入完成以後，其所輸入的的內容會以返回值得形式返回
#   注意：input()的返回值是一個字符串
#   input()函數中可以設置一個字符串作為參數，這個字符串將會作為提示文字顯示
# a = input('請輸入任意內容：')
# print('用戶輸入的內容是:',a)
# input()也可以用於暫時阻止程序結束

# 獲取用戶輸入的用戶名
username = input('請輸入你的用戶名:')
# 判斷用戶名是否是admin
if username == 'admin' :
    print('歡迎管理員光臨！')