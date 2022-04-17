# 顯示歡迎信息
print('-'*20,'歡迎光臨《唐僧大戰白骨精》','-'*20)

# 顯示身份選擇的信息
print('請選擇你的身份：')
print('\t1.唐僧')
print('\t2.白骨精')
# 遊戲的身份選擇
player_choose = input('請選擇[1-2]：')

# 打印一條分割線
print('-'*66)

# 根據用戶的選擇來顯示不同的提示信息
if player_choose == '1':
    # 選擇1
    print('你已經選擇了1，你將以->唐僧<-的身份來進行遊戲！')
elif player_choose == '2':
    # 選擇2
    print('你竟然選擇了白骨精，太不要臉了，你將以->唐僧<-的身份來進行遊戲！')
else :
    # 選擇3
    print('你的輸入有誤，系統將自動分配身份，你將以->唐僧<-的身份來進行遊戲！')

# 進入遊戲

# 創建變量，來保存玩家的生命值和攻擊力
player_life = 2 # 生命值
player_attack = 2 # 攻擊力

# 創建一個變量，保存boss的生命值和攻擊力
boss_life = 10
boss_attack = 10

# 打印一條分割線
print('-'*66)
# 顯示玩家的信息（攻擊力、生命值）
print(f'唐僧，你的生命值是 {player_life} , 你的攻擊力是 {player_attack}')

# 由於遊戲選項是需要反复顯示的，所以必須將其編寫到一個循環中
while True :
    # 打印一條分割線
    print('-'*66)
    # 顯示遊戲選項，遊戲正式開始
    print('請選擇你要進行的操作：')
    print('\t1.練級')
    print('\t2.打BOSS')
    print('\t3.逃跑')
    game_choose = input('請選擇要做的操作[1-3]：')

    # 處理用戶的選擇
    if game_choose == '1' :
        # 增加玩家的生命值和攻擊力
        player_life += 2
        player_attack += 2
        # 顯示最新的信息
        # 打印一條分割線
        print('-'*66)
        # 顯示玩家的信息（攻擊力、生命值）
        print(f'恭喜你升級了！，你現在的生命值是 {player_life} , 你的攻擊力是 {player_attack}')
    elif game_choose == '2' :
        # 玩家攻擊boss
        # 減去boss的生命值，減去的生命值應該等於玩家的攻擊力
        boss_life -= player_attack 

        # 打印一條分割線
        print('-'*66)
        print('->唐僧<- 攻擊了 ->白骨精<-')
        # 檢查boss是否死亡
        if boss_life <= 0 :
            # boss死亡，player勝利，遊戲結束
            print(f'->白骨精<-受到了 {player_attack} 點傷害，重傷不治死了，->唐僧<-贏得了勝利！')
            # 遊戲結束
            break

        # boss要反擊玩家
        # 減去玩家的生命值
        player_life -= boss_attack 
        print(' ->白骨精<- 攻擊了 ->唐僧<-')
        # 檢查玩家是否死亡
        if player_life <= 0 :
            # 玩家死亡
            print(f'你受到了 {boss_attack} 點傷害，重傷不治死了！GAME OVER')
            # 遊戲結束
            break
    elif game_choose == '3' :
        # 打印一條分割線
        print('-'*66)
        # 逃跑，退出遊戲
        print('->唐僧<-一扭頭，撒腿就跑！GAME OVER')
        break
    else :
        # 打印一條分割線
        print('-'*66)
        print('你的輸入有誤，請重新輸入！')