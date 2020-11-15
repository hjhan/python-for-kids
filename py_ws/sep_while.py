# print("请输入一个正整数：", end=' ')
n = int(input("请输入一个正整数："))
i = 0
digits = []  # 列表 list
while (n >= 10 ** i):
    # digit = int(n % 10 ** (i + 1) / 10 ** i)
    digit = n % 10 ** (i + 1) // 10 ** i  # 取出每一位数字
    #digits.insert(0, digit)
    digits.append(digit)
    i += 1

print("每位为%s" % digits)
len = len(digits)
sum = 0
for i in range(len):
    sum += digits[i] * 10 ** (len - i - 1)
print(sum)
