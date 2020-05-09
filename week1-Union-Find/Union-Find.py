'''
1，2，3，4，5，6，7，8，9，0十个数，判断是否在同一个集合中
quick-find的思想是将他们连接，例如：1-2-5，3-4-8-9-0，6-7，然后将2，5的id存为1，4，8，9，0id存为3，7的id存为6，然后id相同的数则在同一个集合
复杂度是n**2
'''
class Quick_Find:
	#生成N数列
	def __init__(self,N):#N个数
		self.array = [num for num in range(N)]#init的意思是当调用Quick_Find这个类时，自动生成一个数列
		
	#将n1，n2两个数据连接起来，例如连接8-9，是将9的id变为8的id（在上述例子中就是将9变为3）
	def union(self,n1,n2):
		for i in range(len(self.array)):
			if self.array[i] == self.array[n1]:
				self.array[i] = self.array[n2]
	
	#判断是否连接
	def is_connected(self,p,q):
		return self.array[p] = self.array[q]
