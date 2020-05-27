class sorting():
    def __init__(self,a):
        self.a = a

    def less(self,i,j):
        return self.a[i] < self.a[j]

    def exchange(self,i,j):
        t = self.a[i]
        self.a[i] = self.a[j]
        self.a[j] = t

    def mergeSort(self,a):
        l = len(self.a)
        '''
        利用递归将left和right进行mergesort
        '''
        if l==1:
            return a.self
        else:
            mid = l//2
            left = self.mergeSort(self.a[:mid])
            right = self.mergeSort(self.a[mid:])

        '''
        将数列sorted的两部分merge成新数列，复制数列，i指示数列前半部分，j指示数列后半部分
        k指示原数列，比较i和j，将小的赋值给k
        '''
        i=j=k=0
        while i < len(left) and j < len(right):
            if left[i]<right[j]:
                self.a[k]=left[i]
                i += 1
            elif left[i]>=right[j]:
                self.a[k]=right[j]
                j += 1
            k+=1

        while i < len(left):
            self.a[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            self.a[k]=right[j]
            j+=1
            k+=1
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
        self.shellSort(self.a)
        print('the string is sorted:%d' %self.isSorted(self.a))
        self.show(self.a)

s=[3,45,5,90,75,2,56,81]
sorting(s).main()
