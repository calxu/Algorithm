#!/usr/bin/python3
# coding:utf-8

# 回溯法-八皇后问题所有可能



def place(row, column):
    """
        限界函数；
        如果一个皇后能放在第row行和column[row]列，则返回true；否则返回false。
        前row行已放置皇后
    """

    i = 0

    while i < row:
        # 不允许同一列；不允许对角线
        if column[i] == column[row] or abs(column[i]-column[row]) == abs(i-row):
            return False

        i += 1

    return True



def n_queen(row, column, n):
    """
        n皇后所有解
    """
    # 初始化放置第一列
    column[row] = 0

    while column[row] < n:
        if place(row, column):
            # 最后一行放置成功
            if row == n - 1:
                print( column )
            else:
                # 下一行
                n_queen( row + 1, column, n )
        
        # 下一列
        column[row] = column[row] + 1



if __name__ == '__main__':
    # 棋盘的大小
    n = 8
    
    # 棋盘上的行
    row = 0 

    # 初始化，第 row 行，第 column[row] 列放置皇后
    column = [0] * n

    n_queen(row, column, n)
