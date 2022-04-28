print('異常出現前')
l = []
try:
    # print(c)
    # l[10]
    # 1 + 'hello'
    print(10/0)
except NameError:
    # 如果except後不跟任何的內容，則此時它會捕獲到所有的異常
    # 如果在except後跟著一個異常的類型，那麼此時它只會捕獲該類型的異常
    print('出現 NameError 異常')
except ZeroDivisionError:
    print('出現 ZeroDivisionError 異常')
except IndexError:
    print('出現 IndexError 異常')
# Exception 是所有異常類的父類，所以如果except後跟的是Exception，他也會捕獲到所有的異常
# 可以在異常類後邊跟著一個 as xx 此時xx就是異常對象
except Exception as e :
    print('未知異常',e,type(e))
finally :
    print('無論是否出現異常，該子句都會執行')

print('異常出現後')