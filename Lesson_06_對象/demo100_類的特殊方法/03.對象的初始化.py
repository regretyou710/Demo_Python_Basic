class Person :
    # 在類中可以定義一些特殊方法（魔術方法）
    # 特殊方法都是以__開頭，__結尾的方法
    # 特殊方法不需要我們自己調用，不要嘗試去調用特殊方法
    # 特殊方法將會在特殊的時刻自動調用
    # 學習特殊方法：
    #   1.特殊方法什麼時候調用
    #   2.特殊方法有什麼作用
    # 創建對象的流程
    # p1 = Person()的運行流程
    #   1.創建一個變量
    #   2.在內存中創建一個新對象
    #   3.__init__(self)方法執行
    #   4.將對象的id賦值給變量

    # init會在對象創建以後立刻執行
    # init可以用來向新創建的對像中初始化屬性
    # 調用類創建對象時，類後邊的所有參數都會依次傳遞到init()中
    def __init__(self,name):
        # print(self)
        # 通過self向新建的對像中初始化屬性
        self.name = name

    def say_hello(self):
        print('大家好，我是%s'%self.name)


# 目前來講，對於Person類來說name是必須的，並且每一個對像中的name屬性基本上都是不同
# 而我們現在是將name屬性在定義為對像以後，手動添加到對像中，這種方式很容易出現錯誤
# 我們希望，在創建對象時，必須設置name屬性，如果不設置對象將無法創建
#   並且屬性的創建應該是自動完成的，而不是在創建對像以後手動完成
# p1 = Person()
# # 手動向對象添加name屬性
# p1.name = '孫悟空'

# p2 = Person()
# p2.name = '豬八戒'

# p3 = Person()
# p3.name = '沙和尚'

# p3.say_hello()

p1 = Person('孫悟空')
p2 = Person('豬八戒')
p3 = Person('沙和尚')
p4 = Person('唐僧')
# p1.__init__() 不要這麼做

# print(p1.name)
# print(p2.name)
# print(p3.name)
# print(p4.name)

p4.say_hello()