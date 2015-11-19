# 判断一个图是否为连通图

K = 1000                                   # 定义类似于无穷大的数
COST = [
    [ K, 10,  K, 30,  45,  K],
    [10,  K, 50,  K,  40, 25],
    [ K, 50,  K,  K,  35, 15],
    [30,  K,  K,  K,   K, 20],
    [45, 40, 35,  K,   K, 55],
    [ K, 25, 15, 20,  55,  K]
]                                        # 边的成本(无向图的权值),置-1方便于从1开始计数


Parent = [-1, -1, -1, -1, -1, -1]        # 父结点


def union(i, j):
    """ 集合并的算法  """
    X = Parent[i] + Parent[j]
    if Parent[i] < Parent[j]:            # 合并后根为i
        Parent[i] = X
        Parent[j] = i
    else:
        Parent[j] = X
        Parent[i] = j


def find(i):
    """ 查找元素i所在的集合的老祖宗 """
    j = i
    while Parent[j] > 0:
        j = Parent[j]
    return j


# 判断一个图是否是连通图
def is_conn(n):
    count = n - 1                         # count记录边的数目(n个顶点的无向图至少有n-1条边)
    for i in range(n):
        for j in range(i+1):           # 遍历下三角每条边的权值
            # print(i, j)
            if COST[i][j] != K:
                u = find(i); v = find(j) # 查找i, j的父亲
                if u != v:               # 如果不是同一个父亲则合并两个集合
                    union(u, v)
                    count -= 1           # 添加一条边，故边的总数-1

                if count == 0:           # 如果添加了n-1条边,则合并了n个集合，故是连通图
                    return True

    return False


# 测试代码
if __name__ == '__main__':
    print(is_conn(6))
