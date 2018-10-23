# Kruskal算法

K = 1000    # 定义类似于无穷大的数
COST = [
    [-1, -1, -1, -1, -1,  -1, -1],
    [-1,  K, 10,  K,  30,  45, K],
    [-1, 10,  K, 50,  K,  40, 25],
    [-1,  K, 50,  K,  K,  35, 15],
    [-1, 30,  K,  K,  K,   K, 20],
    [-1, 45, 40, 35,  K,   K, 55],
    [-1,  K, 25, 15, 20,  55,  K]
]      # 边的成本,置-1方便于从1开始计数


Parent = [0, -1, -1, -1, -1, -1, -1]  # 父结点


def union(i, j):
    """ 集合并的算法  """
    X = Parent[i] + Parent[j]
    if Parent[i] < Parent[j]:      # 合并后根为i
        Parent[i] = X
        Parent[j] = i
    else:
        Parent[j] = X
        Parent[i] = j


def find(i):
    """ 查找元素i所在的集合 """
    j = i
    while Parent[j] > 0:
        j = Parent[j]
    return j


# 将边的权代价按从小到大排序
def least():
    cost = []
    for i in range(1, 7):
        for j in range(1, i+1):
            if COST[i][j] != K:
                cost.append((i, j, COST[i][j]))
    cost = sorted(cost, key=lambda c: c[2], reverse=True)
    return cost


def Kruskal(n):
    """ 最小生成树贪心算法-Kruskal """
    mincost = i = 0
    T = [[0, 0] for i in range(n-1)]    # 将边的顶点初始化为0
    cost = least()                      # 按边成本排序后的列表
    while i < n - 2:
        if not cost:
            break
        e = cost.pop()           # 从COST数组中选最小权的边(u,v)
        u = e[0]; v = e[1]       # 最小权边的两个端点
        j = find(u); k = find(v) # 寻找元素i所在的集合
        if k != j:
            i += 1
            T[i][0] = u;T[i][1] = v
            mincost += COST[u][v]
            union(j, k)

    if i != n-2:
        print('no spanning tree')
        return

    print('生成路径:', T[1:])
    return mincost

if __name__ == '__main__':
    print('最小生成树代价:', Kruskal(7))
