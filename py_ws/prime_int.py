"""
输入一个正整数判断它是不是素数

"""
num = int(input('请输入一个正整数: '))
end = int(num ** 0.5) + 1
is_prime = True
for x in range(2, end):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')
