class A(object):
    def test(self):
        print('AAA')

class B(object):
    def test(self):
        print('B中的test()方法~~')

    def test2(self):
        print('BBB') 

# 在Python中是支持多重繼承的，也就是我們可以為一個類同時指定多個父類
#   可以在類名的()後邊添加多個類，來實現多重繼承
#   多重繼承，會使子類同時擁有多個父類，並且會獲取到所有父類中的方法
# 在開發中沒有特殊的情況，應該盡量避免使用多重繼承，因為多重繼承會讓我們的代碼過於復雜
# 如果多個父類中有同名的方法，則會先在第一個父類中尋找，然後找第二個，然後找第三個。 。 。
#   前面父類的方法會覆蓋後面父類的方法
class C(A,B):
    pass

# 類名.__bases__ 這個屬性可以用來獲取當前類的所有父類    
# print(C.__bases__) (<class '__main__.B'>,)
# print(B.__bases__) (<class 'object'>,)

# print(C.__bases__) # (<class '__main__.A'>, <class '__main__.B'>)

c = C()

c.test()