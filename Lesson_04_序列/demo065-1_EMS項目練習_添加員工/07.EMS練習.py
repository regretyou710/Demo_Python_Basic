# 顯示系統的歡迎信息
print('-'*20 , '歡迎使用員工管理系統', '-'*20)
# 創建一個列表，用來保存員工的信息，員工的信息以字符串的形式統一保存到列表
emps = ['孫悟空\t18\t男\t花果山','豬八戒\t28\t男\t高老莊']

# 創建一個死循環
while True:
    # 顯示用戶的選項
    print('請選擇要做的操作：')
    print('\t1.查詢員工')
    print('\t2.添加員工')
    print('\t3.刪除員工')
    print('\t4.退出系統')
    user_choose = input('請選擇[1-4]:')
    print('-'*62)
    # 根據用戶的選擇做相關的操作
    if user_choose == '1' :
        # 查詢員工
        # 打印表頭
        print('\t序號\t姓名\t年齡\t性別\t住址')
        # 創建一個變量，來表示員工的序號
        n = 1
        # 顯示員工信息
        for emp in emps :
            print(f'\t{n}\t{emp}')
            n += 1
    elif user_choose == '2':
        # 添加員工
        pass
    elif user_choose == '3':
        # 刪除員工
        pass
    elif user_choose == '4':
        # 退出
        print('歡迎使用！再見!')
        input('點擊回車鍵退出！')
        break
    else :
        print('您的輸入有誤，請重新選擇！')

    # 打印分割線
    print('-'*62)