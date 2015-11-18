# 最坏情况时间是O(n)的选择算法 

import math
import random


# 交换下标数组为m和n的位置
def inter_change(A, m, n):
    temp = A[m]
    A[m] = A[n]
    A[n] = temp


# 普通插入排序,数组A类似于['Mark', 8, 1, 8]的形式
def insertion_sort(A, m, n):
    """ 将A中的元素按非降次序分类. """
    j = m + 1
    while j <= n:
        item = A[j]
        i = j - 1
        while (i >= m) and (item < A[i]):
            A[i+1] = A[i]
            i -= 1
        A[i+1] = item
        j += 1


# 快速排序的partition
def partition(A, low, high):
    t = A[low]
    while low < high:
        while low < high and A[high] >= t:
            high -= 1
        A[low] = A[high]

        while low < high and A[low] <= t:
            low += 1

        A[high] = A[low]

    A[low] = t
    return low


r = 5      # 将n个元素分为若干组,每组有r个元素
n = 30     # 数组元素的总个数


# 在数据区间m,p之间选择第k小的元素
def SEL(A, m, p, k):
    """
    返回一个i,使得i属于[m, p],且A(i)是A(m:p)中第k小元素,r是一个全程变量,其取值为大于1的整数
    """
    if p - m + 1 <= r:
        insertion_sort(A, m, p)
        return m+k-1

    while True:
        n = p - m + 1
        for i in range(1, n//r+1):
            insertion_sort(A, m+(i-1)*r, m+i*r-1)
            # 把中间值收集到A(m:p)的前部
            inter_change(A, m+i-1, m+(i-1)*r+r//2-1)

        j = SEL(A, m, m+n//r-1, math.ceil(n/r/2))    # mm
        inter_change(A, m, j)               # 产生划分元素
        j = p
        j = partition(A, m, j)
        if j-m+1 == k:
            return j
        elif j-m+1 > k:
            p = j - 1
        else:
            k -= j - m + 1
            m = j + 1


# 测试代码
if __name__ == '__main__':
    for i in range(3):
        A = random.sample(range(0, 100), 30)    # 随机生成30个数的列表
        A.insert(0, 'START')

        i = SEL(A, 1, 30, 8)

        print('原始的A数组为:', A)
        print('第', 8, '小的元素为:', A[i])
