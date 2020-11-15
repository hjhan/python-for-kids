"""用1,2,3,…,9组成3个三位数abc，def和ghi，每个数字恰好使用一次，
要求abc:def:ghi=1:2:3。输出所有解   数组存储每一位
"""


def setFlag(num: int):
    i = num // 100
    j = num // 10 % 10
    k = num % 10
    a[i] = 1
    a[j] = 1
    a[k] = 1


for abc in range(123, 329):
    a = [0 for i in range(10)]
    d = abc * 2
    ghi = abc * 3

    setFlag(abc)
    setFlag(d)
    setFlag(ghi)

    count = sum(a[1:])

    if (count == 9):
        print("***" + str(a))
        print(abc, d, ghi)
