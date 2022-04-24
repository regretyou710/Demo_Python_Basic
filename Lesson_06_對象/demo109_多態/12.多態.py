# 多態是面向對象的三大特徵之一
# 多態從字面上理解是多種形態
# 狗（狼狗、藏獒、哈士奇、古牧 。。。）
# 一個對象可以以不同的形態去呈現

# 定義兩個類
class A:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self,name):
        self._name = name   

class B:
    def __init__(self,name):
        self._name = name

    def __len__(self):
        return 10

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self,name):
        self._name = name   

class C:
    pass


a = A('孫悟空')
b = B('豬八戒')
c = C()

# 定義一個函數
# 對於say_hello()這個函數來說，只要對像中含有name屬性，它就可以作為參數傳遞
#   這個函數並不會考慮對象的類型，只要有name屬性即可
def say_hello(obj):
    print('你好 %s'%obj.name)

# 在say_hello_2中我們做了一個類型檢查，也就是只有obj是A類型的對象時，才可以正常使用，
#   其他類型的對像都無法使用該函數，這個函數就違反了多態
# 違反了多態的函數，只適用於一種類型的對象，無法處理其他類型對象，這樣導致函數的適應性非常的差
# 注意，向isinstance()這種函數，在開發中一般是不會使用的！
def say_hello_2(obj):
    # 做類型檢查
    if isinstance(obj , A):
        print('你好 %s'%obj.name)    
# say_hello(b)    
# say_hello_2(b)

# 鴨子類型
# 如果一個東西，走路像鴨子，叫聲像鴨子，那麼它就是鴨子

# len()
# 之所以一個對象能通過len()來獲取長度，是因為對像中具有一個特殊方法__len__
# 換句話說，只要對像中具有__len__特殊方法，就可以通過len()來獲取它的長度
l = [1,2,3]
s = 'hello'

# print(len(l))
# print(len(s))
print(len(b))
print(len(c))

# 面向對象的三大特徵：
#   封裝
#       - 確保對像中的數據安全
#   繼承
#       - 保證了對象的可擴展性
#   多態
#       - 保證了程序的靈活性