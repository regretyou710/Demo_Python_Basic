a = int(10) # 創建一個int類的實例
b = str('hello') # 創建一個str類的實例

# print(a , type(a))
# print(b , type(b))

# 定義一個簡單的類
# 使用class關鍵字來定義類，語法和函數很像！
# class 類名([父類]):
#   代碼塊
# <class '__main__.MyClass'>
class MyClass():
    pass

# print(MyClass)
# 使用MyClass創建一個對象
# 使用類來創建對象，就像調用一個函數一樣
mc = MyClass() # mc就是通過MyClass創建的對象，mc是MyClass的實例
mc_2 = MyClass()
mc_3 = MyClass()
mc_4 = MyClass()
# mc mc_2 mc_3 mc_4 都是MyClass的實例，他們都是一類對象
# isinstance()用來檢查一個對像是否是一個類的實例
result = isinstance(mc_2,MyClass)
result = isinstance(mc_2,str)

# print(mc , type(mc))
# print('result =',result)

# print(id(MyClass) , type(MyClass))

# 現在我們通過MyClass這個類創建的對像都是一個空對象
# 也就是對像中實際上什麼都沒有，就相當於是一個空的盒子
# 可以向對像中添加變量，對像中的變量稱為屬性
# 語法：對象.屬性名 = 屬性值
mc.name = '孫悟空'
mc_2.name = '豬八戒'

print(mc_2.name)