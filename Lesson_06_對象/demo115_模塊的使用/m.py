# 可以在模塊中定義變量，在模塊中定義的變量，在引入模塊後，就可以直接使用了
a = 10
b = 20

# 添加了_的變量，只能在模塊內部訪問，在通過import * 引入時，不會引入_開頭的變量
_c = 30

# 可以在模塊中定義函數，同樣可以通過模塊訪問到
def test():
    print('test')

def test2():
    print('test2')

# 也可以定義類    
class Person:
    def __init__(self):
        self.name = '孫悟空'

# 編寫測試代碼，這部分代碼，只要噹噹前文件作為主模塊的時候才需要執行
#   而當模塊被其他模塊引入時，不需要執行的，此時我們就必須要檢查當前模塊是否是主模塊  
if __name__ == '__main__':
    test()
    test2()
    p = Person()
    print(p.name)