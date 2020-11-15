for i in range(1, 10):
    for j in range(1, i+1):
        # print("{0}*{1}={2:<2d}".format(j, i, j * i), end=" ")
        #print(str(j) + "*" + str(i) + "=" + str(i * j) + "\t", end="")
        # print('%d*%d=%d' % (i, j, i * j), end='\t')
        print(f'{j}*{i}={j*i}', end='\t')    # 3.6版本支持的 格式化打印语法
    print("")
