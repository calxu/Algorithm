grap_in = {'0': [],
           '1': [('0', 9)],
           '2': [('0', 7)],
           '3': [('0', 3)],
           '4': [('0', 2)],
           '5': [('1', 1), ('2', 2)],
           '6': [('1', 2), ('2', 7), ('4', 11)],
           '7': [('1', 1), ('3', 11), ('4', 8)],
           '8': [('5', 6), ('6', 4)],
           '9': [('5', 5), ('6', 3), ('7', 5)],
           '10': [('7', 6)],
           '11': [('8', 4), ('9', 2), ('10', 5)]
           }          # K段图字典形式的表示(入边表)


# 多段图-向后处理算法
def f_graph(k, n):
    cost = [100] * n
    d = [0] * n
    p = [''] * k

    cost[0] = 0                   # 将多段图最后一个结点置0
    for i in range(1, n):        # 遍历 1-11 结点的多段图
        e = grap_in[str(i)]       # i所有的入度的边

        for s in e:
            m = cost[int(s[0])] + s[1]       # 设r是一个这样的结点,<i,r>是边,且使 cost(r)+c(r, i) 取最小值
            if m < cost[i]:
                cost[i] = m                  # 使 c(i, r)+cost(r) 取最小值
                d[i] = s[0]                  # 记录当前结点的下一个结点

    p[0] = '0'; p[k-1] = str(n-1)           # 将开始结点 和 结束结点 初始化
    for j in range(k-2, 0, -1):             # 计算其余k-2个结点
        p[j] = d[int(p[j+1])]                # p[j+1]记录当前结点的下一个最短路径结点

    print(p)                                 # 输出最短路径
    print(cost[11])

if __name__ == '__main__':
    f_graph(5, 12)          # k=5(即5段图),共12个结点
