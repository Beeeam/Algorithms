class sorting():
    def __init__(self,a):
        self.a = a

    def less(self,i,j):
        return self.a[i] < self.a[j]

    def exchange(self,i,j):
        t = self.a[i]
        self.a[i] = self.a[j]
        self.a[j] = t
        # 冒泡排序每次比较相邻两个元素大小，每次循环会完成最大元素的排序，交换n**2次
    def bubbleSort(self,a):
        l = len(self.a)
        for i in range(l-1):
            for j in range(l-i-1):
                if not self.less(j,j+1):
                    self.exchange(j,j+1)
        return self.a
    
    #每个循环找到剩下的数中最小的，将最小的与循环次数相对应的那一项进行交换，比较n**2次
    def selectionSort(self,a):
        l = len(self.a)
        for i in range(l-1):
            min = i
            for j in range(i+1,l):
                if self.less(j,min):
                    min = j
            self.exchange(i,min)
        return self.a

    #ij两个指针从左往右移动，如果当前的数字比左边的数小，则进行交换直到左边的数字全部完成排序
    def insertionSort(self,a):
        l = len(self.a)
        for i in range(l):
            j = i
            while j>0:
                if self.less(j,j-1):
                    self.exchange(j,j-1)
                else:
                    break
                j -= 1
        return self.a

    #每隔h个数字构造一个子数列，对于子数列使用insertionSort，间隔h按照3h+1进行选定，h递减,N**3/2
    def shellSort(self,a):
        l = len(self.a)
        h =1
        while h <l//3:
            h = 3*h+1 #1 4 13 40 121 ……
        while h >0:
            for i in range(h,l):
                j = i
                while j>=h:
                    if self.less(j,j-h):
                        self.exchange(j,j-h)
                    else:
                        break
                    j -= h
            h //= 3
        return self.a


    def isSorted(self,a):
        l= len(self.a)
        for i in range(l):
            if self.less(i,i+1):
                return True
        return False

    def show(self,a):
        l = len(self.a)
        print('the sorted list is:')
        for i in range(l):
            print(a[i],end=' ')

    def main(self):
        self.bubbleSort(self.a)
        print('the string is sorted:%d' %self.isSorted(self.a))
        self.show(self.a)

s=[3,45,5,90,75,2,56,81]
sorting(s).main()
