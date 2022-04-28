# print('hello')
# try:
#     # try中放置的是有可能出現錯誤的代碼
#     print(10/0)
# except:
#     # except中放置的是出錯以後的處理防暑
#     print('哈哈哈，出錯了~~~')
# else:
#     print('程序正常執行沒有錯誤')    
# print('你好')


# print(10/0)


def fn():
    print('Hello fn')
    print(a)
    print(10/0)

def fn2():
    print('Hello fn2')
    fn()

def fn3():
    print('Hello fn3')
    fn2()

fn3()