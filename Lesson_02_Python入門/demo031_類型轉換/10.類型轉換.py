# 類型轉換四個函數 int() float() str() bool()
# int() 可以用來將其他的對象轉換為整型
# 規則：
#   布爾值：True -> 1   False -> 0
#   浮點數：直接取整，省略小數點後的內容
#   字符串：合法的整數字符串，直接轉換為對應的數字
#           如果不是一個合法的整數字符串，則報錯 ValueError: invalid literal for int() with base 10: '11.5'
#   對於其他不可轉換為整型的對象，直接拋出異常 ValueError
# float() 和 int()基本一致，不同的是它會將對象轉換為浮點數
# str() 可以將對象轉換為字符串
#  True -> 'True'
#  False -> 'False'
#  123 -> '123' 
#  。 。 。
#  bool() 可以將對象轉換為布爾值，任何對像都可以轉換為布爾值
#   規則：對於所有表示空性的對像都會轉換為False，其餘的轉換為True
#       哪些表示的空性：0 、 None 、 '' 。 。 。

a = True

# 調用int()來將a轉換為整型
# int()函數不會對原來的變量產生影響，他是對象轉換為指定的類型並將其作為返回值返回
# 如果希望修改原來的變量，則需要對變量進行重新賦值
a = int(a)

a = False
a = int(a)

a = '123'
a = int(a)

a = 11.6
a = int(a)

a = '11.5'
# a = int(a)

a = None
# a = int(a)

a = 1
a = float(a)

a = False
a = float(a)

a = 123
a = str(a)

a = None
a = bool(a)

print('a =',a)
print('a的類型是',type(a))
# b = 456
# print('hello'+str(b))