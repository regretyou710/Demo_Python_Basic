# 第四章 序列（視頻58-76）
## 列表（list）
    - 列表是Python中的一個對象
    - 對象（object）就是內存中專門用來存儲數據的一塊區域
    - 之前我們學習的對象，像數值，它只能保存一個單一的數據
    - 列表中可以保存多個有序的數據
    - 列表是用來存儲對象的對象
    - 列表的使用：
        1.列表的創建
        2.操作列表中的數據

    - 練習：
        - 創建一個列表，在列表中保存你最好的5個朋友的名字
            然後分別通過索引來獲取每一個朋友的名字

## 序列（sequence）
    - 序列是Python中最基本的一種數據結構
    - 數據結構指計算機中數據存儲的方式
    - 序列用於保存一組有序的數據，所有的數據在序列當中都有一個唯一的位置（索引）
        並且序列中的數據會按照添加的順序來分配索引
    - 序列的分類：
        可變序列（序列中的元素可以改變）：
            > 列表（list）
        不可變序列（序列中的元素不能改變）：
            > 字符串（str）    
            > 元組（tuple）
        - 剛剛我們所講所有操作都是序列的通用操作01 02 03 三個文件中的操作
        
## EMS（Employee Manager System 員工管理系統） 練習
    - 做命令行版本的員工管理系統
    - 功能：
        四個：
            1.查詢
                - 顯示當前系統當中的所有員工
            2.添加
                - 將員工添加到當前系統中
            3.刪除
                - 將員工從系統當中刪除
            4.退出
                - 退出系統
    - 員工信息要保存到哪裡？列表，在系統中應該有一個列表，專門用來保存所有員工信息的 

## 可變對象
    - 每個對像中都保存了三個數據：
        id（標識）
        type（類型）
        value（值）    

    - 列表就是一個可變對象
        a = [1,2,3]

    - a[0] = 10 （改對象）
        - 這個操作是在通過變量去修改對象的值
        - 這種操作不會改變變量所指向的對象    
        - 當我們去修改對象時，如果有其他變量也指向了該對象，則修改也會在其他的變量中體現

    - a = [4,5,6] （改變量）
        - 這個操作是在給變量重新賦值
        - 這種操作會改變變量所指向的對象
        - 為一個變量重新賦值時，不會影響其他的變量

    - 一般只有在為變量賦值時才是修改變量，其餘的都是修改對象

## 字典（dict）
    - 字典屬於一種新的數據結構，稱為映射（mapping）
    - 字典的作用和列表類似，都是用來存儲對象的容器
    - 列表存儲數據的性能很好，但是查詢數據的性能的很差
    - 在字典中每一個元素都有一個唯一的名字，通過這個唯一的名字可以快速的查找到指定的元素
    - 在查詢元素時，字典的效率是非常快的
    - 在字典中可以保存多個對象，每個對像都會有一個唯一的名字
        這個唯一的名字，我們稱其為鍵（key），通過key可以快速的查詢value
        這個對象，我們稱其為值（value）
        所以字典，我們也稱為叫做鍵值對（key-value）結構
        每個字典中都可以有多個鍵值對，而每一個鍵值對我們稱其為一項（item）

## 集合（set）
    - 集合和列表非常相似
    - 不同點：
        1.集合中只能存儲不可變對象
        2.集合中存儲的對像是無序（不是按照元素的插入順序保存）
        3.集合中不能出現重複的元素