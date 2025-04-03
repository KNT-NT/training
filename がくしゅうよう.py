import random

def play_game():
    correct_num = random.randint(1, 50)
    count = 0
    while count < 3:
        guess = int(input("1〜50の数字を入力してください: "))
        if guess < correct_num:
            print("もっと大きいよ")
            count += 1
        elif guess > correct_num:
            print("もっと小さいよ")
            count += 1
        else:
            print("正解！")
            break

play_game()

while True:
    replay = input("またやる？")
    if replay == "y":
        play_game()
    elif replay == "n":
        print('お疲れ様でした')
        break
    else:
        print('yかnで答えてください。')
