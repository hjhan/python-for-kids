names = "诸葛亮，曹操,刘备,关羽,张飞,孙权"

for n in names:
    if (n == ',' or n == '，'):
        print()  # 换行
        continue
    print(n, end='')
    pass
