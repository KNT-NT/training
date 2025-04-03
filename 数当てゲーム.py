import random

def game(choose_num):
    correct_num = random.randint(1, 101) #1から100までの数字で数当てゲーム。
    if choose_num == correct_num:
        print("よりも小さいよ")
    elif choose_num >= correct_num:
        print("よりも小さいよ")
    else:
        print("正解！")

game(int(input("数字を入力してください")))