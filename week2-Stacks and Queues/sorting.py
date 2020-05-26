class sorting():
    def __init__(self,a):
        self.a = a

    def less(self,i,j):
        return self.a[i] < self.a[j]

    def exchange(self,i,j):
        t = self.a[i]
        self.a[i] = self.a[j]
        self.a[j] = t
    # 冒泡排序每次比较相邻两个元素大小，每次循环会完成最大元素的排序
    def bubbleSort(self,a):
        l = len(self.a)
        for i in range(l-1):
            for j in range(l-i-1):
                if not self.less(j,j+1):
                    self.exchange(j,j+1)
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
