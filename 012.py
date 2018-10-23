# 基本检索与周游方法-双连通分图和深度优先检索

from collections import Counter

# 任意一个无向图的邻接表表示
grap = {1: [2, 4],
        2: [1, 3, 5, 7, 8],
        3: [2, 4, 9, 10],
        4: [1, 3],
        5: [2, 6, 7, 8],
        6: [5],
        7: [2, 5, 8],
        8: [2, 5, 7],
        9: [3],
        10:[3]
       }

DFN = [0] * 11      # DFN是全程量,并将其初始化为0
L = [0] * 11        # L是全程量,并将其初始化为0
num = 1             # num是全程量,被初始化为1
stack = []          # 模拟栈的作用
Point = []          # 连通分图的各点


def ART(u, v=1):
    """
    u是深度优先检索的开始结点。在深度优先生成树中，u若
    有父亲，那么v就是它的父亲(v初始化为-1)。
    """
    global DFN, L, num
    DFN[u] = num; L[u] = num; num += 1

    for w in grap[u]:   # 遍历每一个邻接于u的结点
        # 1.树枝:如w未被访问,则DFN(w)=0,此时,DFN(w)<DFN(u)成立
        # 2.逆边: DFN(w)< DFN(u)成立
        if v != w and DFN[w] < DFN[u]:
            # 注意: 若v=w或DFN(w)>DFN(u)表明(u, w)是在栈中,现(u, w)是未在栈中的树枝或逆边
            stack.append((u, w))

        if DFN[w] == 0:
            ART(w, u)    # 还未访问w,则递归调用
            # 表示u为割点,因为u的儿子w子孙路径加一条逆边到不了u的祖先,则一个双连通分图形成了
            if L[w] >= DFN[u]:
                print("双连通分图:")
                p = set()                    # 边
                while True:
                    x, y = stack.pop()
                    p.add(x); p.add(y)       # 将结点添加进集合
                    print('(', x, ',', y, ')')
                    if (x, y) == (u, w) or (x, y) == (w, u):
                        break
                Point.append(p)

            L[u] = min(L[u], L[w])
        elif w != v:    # w不是u的父亲
            L[u] = min(L[u], DFN[w])  # (u, w)是一条逆边

# 测试代码
if __name__ == '__main__':
    ART(1)

    count = Counter([i for t in Point for i in t])       # 计算每个顶点在各双连通分图合计出现的次数
    cut_point = [i for i in count if count[i]>1]         # 出现次数大于1的即为割点
    print('割点为：', *cut_point)                         # 打印输出割点

    print('需要加入的边为:')
    for p in cut_point:                                   # 遍历割点
        for g in Point:                                   # 遍历双连通分图中
            if p in g:                                    # 割点在双连通分图中
                t = (g - {p}).pop()                        # 任取双连通分图中除割点以外的任意一点
                print(t, end=' ')                         # 将该点视为将要连接的点
        print('之间')
