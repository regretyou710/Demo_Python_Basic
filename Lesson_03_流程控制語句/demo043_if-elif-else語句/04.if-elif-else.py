# if-elif-else語句
# 語法：
#   if 條件表達式 :
#       代碼塊
#   elif 條件表達式 :
#       代碼塊
#   elif 條件表達式 :
#       代碼塊
#   elif 條件表達式 :
#       代碼塊
#   else :
#       代碼塊
#       
# 執行流程：
#   if-elif-else語句在執行時，會自上向下依次對條件表達式進行求值判斷，
#       如果表達式的結果為True，則執行當前代碼塊，然後語句結束
#       如果表達式的結果為False，則繼續向下判斷，直到找到True為止
#       如果所有的表達式都是False，則執行else後的代碼塊
#   if-elif-else中只會有一個代碼塊會執行

age = 210

# if age > 200 :
#     print('活著可真沒勁呢！')
# elif age > 100 :
#     print('你也是老大不小了！')
# elif age >= 60 :
#     print('你已經退休了！')
# elif age >= 30 :
#     print('你已經是中年了！')
# elif age >= 18 :
#     print('你已經成年了！')
# else :
#     print('你還是個小孩！')

age = 68

if age >= 18 and age < 30 :
    print('你已經成年了！')
elif age >= 30 and age < 60 :
    print('你已經中年了！')
elif age >= 60 :
    print('你已經退休了！')