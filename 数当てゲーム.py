import random

def game(choose_num):
    correct_num = random.randint(1, 101) #1から100までの数字で数当てゲーム
    if choose_num < correct_num: #入力した数字が答えより大きい時
        print("よりも小さいよ")
    elif choose_num > correct_num: #入力した数字が答えより小さい時
        print("よりも小さいよ")
    else: #入力した数字と正解が一致したとき
        print("正解！")

game(int(input("数字を入力してください")))