# coding: utf-8
__author__ = 'leemo'

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import os

cwp = os.path.dirname(os.path.abspath(__file__))

"""
给定一个数字三角形，找到从顶部到底部的最小路径和。每一步可以移动到下面一行的相邻数字上。
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
从顶到底部的最小路径和为11 ( 2 + 3 + 5 + 1 = 11)。

解题思路：
使用动态规划, table[i][j],表示从顶层到第i底层第j个元素的最短路径，整个过程就是填表的过程，使用自顶向下
minimun_path[i] = min(table[i])
table[i][j] = min(table[i-1][j], table[i-1][j+1]) + triangle[i][j]
其中，如果table[i][j]不存在，则说明路径无穷大
"""


def dynamic_programming(triangle):
    table = [[999999999 for j in range(len(triangle))] for i in range(len(triangle))]
    table[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(i+1):
            try:
                left = table[i - 1][j]
            except:
                left = 999999999
            try:
                right = table[i - 1][j - 1]
            except:
                right = 999999999
            table[i][j] = min(left, right) + triangle[i][j]
    return table


if __name__ == "__main__":
    table = dynamic_programming([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ])
    print min(table[-1])
