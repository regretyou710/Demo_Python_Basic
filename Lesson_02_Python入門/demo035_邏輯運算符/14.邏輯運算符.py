# 邏輯運算符
# 邏輯運算符主要用來做一些邏輯判斷
# not 邏輯非
#   not可以對符號右側的值進行非運算
#       對於布爾值，非運算會對其進行取反操作，True變False，False變True
#       對於非布爾值，非運算會先將其轉換為布爾值，然後再取反
#       
# and 邏輯與
#   and可以對符號兩側的值進行與運算
#    只有在符號兩側的值都為True時，才會返回True，只要有一個False就返回False
#    與運算是找False的
#    Python中的與運算是短路的與，如果第一個值為False，則不再看第二個值
#   
# or 邏輯或
#   or 可以對符號兩側的值進行或運算
#    或運算兩個值中只要有一個True，就會返回True
#    或運算是找True的
#    Python中的或運算是短路的或，如果第一個值為True，則不再看第二個值
#    
# 練習：
#   嘗試一下對布爾值進行三種邏輯運算
#   嘗試對非布爾值進行三種邏輯運算，並觀察返回的結果   
#   

a = True
a = not a # 對a進行非運算

a = 1
a = ''
a = not a
# print('a =',a)

result = True and True # True
result = True and False # False
result = False and True # False
result = False and False # False

# print(result) 

# True and print('你猜我出來嗎？') 第一個值是True，會看第二個值，所以print()會執行
# False and print('你猜我出來嗎？')第一個值是False，不會看第二個值，所以print()不會執行


result = True or True # True
result = True or False # True
result = False or True # True
result = False or False # False

# print(result) 
# False or print('你猜我出來嗎？') 第一個值為False，繼續看第二個，所以打印語句執行
# True or print('你猜我出來嗎？') 第一個值為True，不看第二個，所以打印語句不執行