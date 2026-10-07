import random

answer = random.randint(1, 10)
guess = int(input("猜一个 1 到 10 的数字："))

if guess == answer:
    print("猜对了！")
else:
    print("没猜中，答案是", answer)

