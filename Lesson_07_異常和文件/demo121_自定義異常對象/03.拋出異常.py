# 也可以自定義異常類，只需要創建一個類繼承Exception即可
class MyError(Exception):
    pass

def add(a,b):
    # 如果a和b中有負數，就向調用處拋出異常
    if a < 0 or b < 0:
        # raise用於向外部拋出異常，後邊可以跟一個異常類，或異常類的實例
        # raise Exception    
        # 拋出異常的目的，告訴調用者這裡調用時出現問題，希望你自己處理一下
        # raise Exception('兩個參數中不能有負數！')  
        raise MyError('自定義的異常')
        
        # 也可以通過if else來代替異常的處理
        # return None
    r = a + b
    return r

print(add(-123,456))