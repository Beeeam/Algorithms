
import numpy as np
import random
import sys
sys.path.append('/Users/beam/Desktop/project/algorithms/UF') 
from union import Quick_Union_Weight as quw
import statistics as stat
import math
class percolation:
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
        if m-1>0 and self.is_open(m-1,n) == 1:
            self.wqu.union(self.id(m,n),self.id(m-1,n))
        if m+1<self.N and self.is_open(m+1,n) ==1:
            self.wqu.union(self.id(m,n),self.id(m+1,n))
        if n-1>0 and self.is_open(m,n-1) == 1:
            self.wqu.union(self.id(m,n),self.id(m,n-1))
        if n+1<self.N and self.is_open(m,n+1) ==1:
            self.wqu.union(self.id(m,n),self.id(m,n+1))
    '''
    A full site is an open site that can be connected to an open site 
    in the top row via a chain of neighboring (left, right, up, down) 
    open sites. 
    '''
    def isfull(self,m,n):
        if self.is_open(m,n) ==1:
            for i in range(self.N):
                if self.wqu.is_connected(self.id(m,n),i) == 1:
                    return True
        return False
    '''
    返回opensite的个数
    '''
    def nmofops(self):
        num = 0
        for m in range(self.N):
            for n in range(self.N):
                num += self.is_open(m,n)
        return num
    '''
    the system percolates if there is a full site in the bottom row. 
    In other words, a system percolates if we fill all open sites connected 
    to the top row and that process fills some open site on the bottom row. 
    '''
    def ispercolated(self):
        for i in range(self.N):
            if self.isfull(self.N,i+1) == 1:
                return True
        return False

class PercolationStats:
        
    '''
    1次运行到percolates，记录opensites，计算fraction，总共percolate 400次，计算
    400个fractions的平均值
    N是grid的大小，T表示实验次数，需要统计percolates之后opensites的数目，用random
    任取(m,n)并将其打开
    '''
    def __init__(self,N,T):
        self.fractions = []
        if N<=0 or T<=0:
            raise Exception('should larger than 0')
        self.times = T
        for i in range(T):
            self.grid = percolation(N)
            self.num = 0
            print(i)
            while not self.grid.ispercolated():
                m = random.randint(1,N)
                n = random.randint(1,N)
                if not self.grid.is_open(m,n):
                    self.grid.open(m,n)
                    self.num+=1
            self.fractions.append(float(self.num/(N*N)))
            print(self.fractions)

    
    def mean(self):
        return float(stat.mean(self.fractions))

    def stddev(self):
        return float(stat.stdev(self.fractions))

    def confidenceLo(self):
        return self.mean() - (1.96*self.stddev())/math.sqrt(self.times)

    def confidenceHi(self):
        return self.mean() + (1.96*self.stddev())/math.sqrt(self.times)

    def main(self):
        print('mean:%f' %self.mean())
        print('stddev:%f' %self.stddev())
        print('0.95 confidence interval: [%f'  % self.confidenceLo() +', %f' %self.confidenceHi()+']')

PercolationStats(5,20).main()
