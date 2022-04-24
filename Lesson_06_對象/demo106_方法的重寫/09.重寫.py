# 繼承

# 定義一個類 Animal（動物）
#   這個類中需要兩個方法：run() sleep() 
class Animal:
    def run(self):
        print('動物會跑~~~')

    def sleep(self):
        print('動物睡覺~~~')


class Dog(Animal):
    def bark(self):
        print('汪汪汪~~~') 

    def run(self):
        print('狗跑~~~~')    


# 如果在子類中如果有和父類同名的方法，則通過子類實例去調用方法時，
#   會調用子類的方法而不是父類的方法，這個特點我們成為叫做方法的重寫（覆蓋，override）
# 創建Dog類的實例
# d = Dog()

# d.run()

# 當我們調用一個對象的方法時，
#   會優先去當前對像中尋找是否具有該方法，如果有則直接調用
#   如果沒有，則去當前對象的父類中尋找，如果父類中有則直接調用父類中的方法，
#   如果沒有，則去父類的父類中尋找，以此類推，直到找到object，如果依然沒有找到，則報錯
class A(object):
    def test(self):
        print('AAA')

class B(A):
    def test(self):
        print('BBB')

class C(B):
    def test(self):
        print('CCC')   

# 創建一個c的實例
c = C()
c.test()