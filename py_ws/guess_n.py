import random
n = random.randint(0, 100)

counter = 0
while True:
    m = int(input("请输入："))
    counter += 1
    if (n > m):
        print("猜小了，继续来")
    elif (n < m):
        print("猜大了，小一点")
    else:
        print("猜中了，恭喜！")
        break
# 当退出while循环的时候显示用户一共猜了多少次
print(f'你总共猜了{counter}次')
if counter > 7:
    print('今天没睡好吗？吃点核桃补补脑子！')
