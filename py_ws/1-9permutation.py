"""用1,2,3,…,9组成3个三位数abc，def和ghi，每个数字恰好使用一次，要求abc:def:ghi=1:2:3。输出所有解"""
"""穷举法，，三个三位数是abc, def, ghi，比率是1:2:3，那么显然d>=(2*a)并且g>=3*a。所以，1<=a<=3，d>=2a，g>=3a；
第一种方法：通过判断1~9的和为45，相乘等于362880来输出
"""


def result(num: int):
    i = num // 100
    j = num // 10 % 10
    k = num % 10
    sum = i + j + k
    # 分解出来的位数相加
    product = i * j * k
    # 相乘
    return sum, product


for i in range(123, 329):
    j = i * 2
    k = i * 3

    result_add = 0
    result_mul = 1

    sum_i, product_i = result(i)
    sum_j, product_j = result(j)
    sum_k, product_k = result(k)
    sum = 0
    sum = sum_i + sum_j + sum_k
    product = product_i * product_j * product_k
    if (sum == 45 and product == 362880):
        print(i, j, k)
