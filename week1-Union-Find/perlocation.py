import numpy as np
import random
import sys
sys.path.append('/Users/beam/Desktop/project/algorithms/UF') 
from union import Quick_Union_Weight as quw

class perlocation:
    '''
    生成一个N**2的矩阵，open用1，full用0
    '''
    def __init__(self,N):
        self.N = N
        self.grid = np.zeros((N,N))
        self.wqu = quw(N*N)
    '''
    判断(m,n)是否是open
    '''
    def is_open(self,m,n):
        return self.grid[m-1][n-1] == 1

    '''
    计算(m,n)位置所对应的id
    '''
    def id(self,m,n):
        return (m-1)*self.N+n-1
    '''
    打开(m,n)位置，即将(m,n)的0变成1，然后将上下左右连接起来,(m,n)对应id中的数字是m*N+n
    '''
    def open(self,m,n):
        self.grid[m-1][n-1] = 1
        if m>=1 & self.is_open(m-1,n) == 1:
            self.wqu.union(self.id(m,n),self.id(m-1,n))
        if m<self.N & self.is_open(m+1,n) ==1:
            self.wqu.union(self.id(m,n),self.id(m+1,n))
        if n>=1 & self.is_open(m,n-1) == 1:
            self.wqu.union(self.id(m,n),self(m,n-1))
        if n<self.N & self.is_open(m,n+1) ==1:
            self.wqu.union(self.id(m,n),self(m,n+1))
    '''
    A full site is an open site that can be connected to an open site 
    in the top row via a chain of neighboring (left, right, up, down) 
    open sites. 
    '''
    def isfull(self,m,n):
        if self.is_open(m,n) ==1:
            for i in range(self.N):
                return self.wqu.is_connected(self.id(m,n),i) == 1
        return False
    '''
    返回opensite的个数
    '''
    def nmofops(self):
        num = 0
        for m,n in range(self.N):
            num += self.is_open(m,n)
            return num
    '''
    the system percolates if there is a full site in the bottom row. 
    In other words, a system percolates if we fill all open sites connected 
    to the top row and that process fills some open site on the bottom row. 
    '''
    def ispercolated(self):
        for i in range(self.N):
            return self.isfull(self.N-1,i) == 1
        return False
