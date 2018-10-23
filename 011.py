# 0/1背包问题的算法

# 书上P141


def PARTS(P, W, F, M, p, w, X, n):
    for i in range(n):      # 循环判断
        L = F[n-i-1]         # S n-i-1 的首端
        H = F[n-i]-1         # S n-i-1 的末端
        px, wx = P[H], W[H]  # (px, wx) = S n-i-1的最末序偶
        py, wy = -1, -1

        # W[j]是S n-i-1中使得 W[j]+w[n-i]<=M 的所有序偶中取最大值的W[j]
        for j in range(H, L-1, -1):
            if W[j] + w[n-i] <= M:
                py, wy = P[j] + p[n-i], W[j] + w[n-i]
                break

        if px > py:         # px 是S n-i 的最末序偶
            xn = 0
        else:               # py 是S n-i 的最末序偶
            xn = 1
            M -= w[n-i]      # M减去加入背包的重量后还剩的重量

        X.insert(0, xn)      # 确定 Xn, Xn-1, ..., x1

    print(X)                 # 输出0/1背包问题的序列解


def DKNAP(p, w, n, M, m):
    # 初始化变量
    P = [0]*(m + 1); W = [0]*(m + 1)    # P:效益;W:权重  (1:m)有效
    F = [0]*(n + 1)                     # (0:n)有效

    F[0] = 1; P[1] = W[1] = 0           # S0
    L = H = 1                           # S0的首端与末端指针
    F[1] = next = 2                     # P和W中第一个空位

    for i in range(1, n):               # 生成Si
        k = L                           # 指向S i-1 中正在考虑是否并到Si中去的序偶
        j = L

        # 生成序偶,相应的归并工作在这里进行.每次迭代首先生成一对序偶(pp, ww),
        # 接着将S i-1中所有还没有被清除和归并到S i中且有W < ww的序偶(p, w)都并入S
        while j <= H and W[j] + w[i] <= M:
            pp, ww = P[j] + p[i], W[j] + w[i]    # S i1  中的下一个元素

            # 从S i-1 中取元素来归并
            while k <= H and W[k] < ww:
                P[next] = P[k]; W[next] = W[k]
                next += 1; k += 1

            # 处理S i-1 中正在考虑的序偶的W值等于ww时的情况,比较
            # 比较P 和 pp, 将值小的对应序偶清除
            if k <= H and W[k] == ww:
                pp = max(pp, P[k])
                k += 1

            # 在pp >　Ｐ(next-1)的情况下,把序偶(pp, ww)加入到S i中
            if pp > P[next-1]:
                P[next], W[next] = pp, ww
                next += 1

            while k <= H and P[k] <= P[next-1]:    # 清除
                k += 1

            j += 1                                 # 计数值自增1

        # 将 S i-1 中剩余的元素并入 S i
        while k <= H:
            P[next], W[next] = P[k], W[k]
            next += 1; k += 1

        # 对S i+1置初值
        L = H + 1; H = next - 1; F[i+1] = next

    print(P[1:])
    print(W[1:])
    print(F)
    X = []                                          # 0/1背包的解

    PARTS(P, W, F, M, p, w, X, n)                   # P 效益数组；W 重量数组； F每个S的下标； M剩余的重量
                                                    # p条件中效益；w条件中重量；Ｘ 0/1背包的解；n包的个数


if __name__ == '__main__':
    p = [0, 2, 5, 8, 1]; w = [0, 10, 15, 6, 9]    # p效益, w权重
    n = 4; M = 30; m = 30                         # n背包的个数; M剩余的重量; m数组的长度
    DKNAP(p, w, n, M, m)
