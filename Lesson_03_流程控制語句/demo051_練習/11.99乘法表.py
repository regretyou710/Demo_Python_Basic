# 練習1：
#   打印99乘法表
#   1*1=1
#   1*2=2 2*2=4
#   1*3=3 2*3=6 3*3=9
#   ...                 9*9=81

# 創建一個外層循環來控製圖形的高度
i = 0
while i < 9:
    i += 1
    
    # 創建一個內層循環來控製圖形的寬度
    j = 0
    while j < i:
        j += 1
        print(f"{j}*{i}={i*j} ",end="")

    print()