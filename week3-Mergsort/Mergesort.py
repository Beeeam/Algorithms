class sorting():
    def __init__(self,a):
        self.a = a

    def less(self,i,j):
        return self.a[i] < self.a[j]

    def exchange(self,i,j):
        t = self.a[i]
        self.a[i] = self.a[j]
        self.a[j] = t



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
        self.shellSort(self.a)
        print('the string is sorted:%d' %self.isSorted(self.a))
        self.show(self.a)
