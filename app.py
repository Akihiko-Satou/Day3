import random

answer = random.randint(1, 100)

count = 0

print("数当てゲームをします！1～100の数を当ててください")

print("当たるまで続きます！何回目で当てられるかな？")

while True:
    try:
        guess = int(input("1～100までの数を入力してください："))
        count += 1

        if guess == answer:
            print(f"正解！{count}回で当たりました！")
            break
        elif guess < answer:
            print("もっと大きいよ")
        else:
            print("もっと小さいよ")

    except ValueError:
        print("数を入力してください")
        continue



