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
        # 獲取要添加員工的信息，姓名、年齡、性別、住址
        emp_name = input('請輸入員工的姓名：')
        emp_age = input('請輸入員工的年齡：')
        emp_gender = input('請輸入員工的性別：')
        emp_address = input('請輸入員工的住址：')

        # 創建員工信息
        # 將四個信息拼接為一個字符串，然後插入到列表中
        emp = f'{emp_name}\t{emp_age}\t{emp_gender}\t{emp_address}'
        # 顯示一個提示信息
        print('以下員工將被添加到系統中')
        print('-'*62)
        print('姓名\t年齡\t性別\t住址')
        print(emp)
        print('-'*62)
        user_confirm = input('是否確認該操作[Y/N]:')

        # 判斷
        if user_confirm == 'y' or user_confirm == 'yes' :
            # 確認
            emps.append(emp)
            # 顯示提示信息
            print('添加成功！')
        else :
            # 取消操作
            print('添加已取消！')
        
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