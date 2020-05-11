'''
1，2，3，4，5，6，7，8，9，0十个数，判断是否在同一个集合中
quick-find的思想是将他们连接，例如：1-2-5，3-4-8-9-0，6-7，然后将2，5的id存为1，4，8，9，0id存为3，7的id存为6，然后id相同的数则在同一个集合
复杂度是n**2
'''
class Quick_Find:
	#生成N数列
	def __init__(self,N):#N个数
		self.id = [num for num in range(N)]#init的意思是当调用Quick_Find这个类时，自动生成一个数列
		
	#将n1，n2两个数据连接起来，例如连接8-9，是将9的id变为8的id（在上述例子中就是将9变为3）
	def union(self,p,q):
		for i in range(len(self.array)):
			if self.id[i] == self.id[p]:
				self.id[i] = self.id[q]
	
	#判断是否连接
	def is_connected(self,p,q):
		return self.id[p] = self.id[q]

'''
quick-union的思想是将他们做成树，例如：1-2-5，3-4要将4，5连接就是找到他们的根，1，3，然后将3变成1的child
复杂度是n
'''
class Quick_Union:
	def __init__(self,N):
		self.id = [num for num in range(N)]
	
	#判断一个数的根，如果这个数的id是本身则就是根，否则将id作为要找的数继续寻找	
	def root(self,i):
		while i != self.id[i]:
			i = self.id[i]
		return i
	
	#将两个数连接起来，先找到两个数的根，如果不同就将一个作为另一个的child
	def union(self,p,q):
		pid = self.root(p)
		qid = self.root(q)
		self.id[pid] = qid
		
	#判断是否在一棵树上
	def is_connected(self,p,q):
		return self.root(p) == self.root(q)
'''
quick-union在树很高的时候会导致计算量变大，一个改进方法是总是将小树连接到大树上而不是反过来
复杂度是lgN
'''
class Quick_Union_Weight:
	def __init__(self,N):
		self.id = [num for num in range(N)]
		self.size = [1 for i in range(N)]#每个nodes初始size是1
	
	#判断一个数的根，如果这个数的id是本身则就是根，否则将id作为要找的数继续寻找	
	def root(self,i):
		while i != self.id[i]:
			i = self.id[i]
		return i
	
	#将两个数连接起来，先找到两个数的根，如果不同就计算树的size，将小的树作为大的树的child
	def union(self,p,q):
		pid = self.root(p)
		qid = self.root(q)
		if pid != qid:
			if self.size[pid] < self.size[qid]:
				self.id[pid] = qid
				self.size[qid] += self.size[pid]
			else:
				self.id[qid] = pid
				self.size[pid] += self.size[qid]
		
	#判断是否在一棵树上
	def is_connected(self,p,q):
		return self.root(p) == self.root(q)
'''
path compression是修剪太高的树，找到某个root，将他们直接连到grandparent上，找到root后将id[i]=id[id[i]]
'''
class QUWPC:
	def __init__(self,N):
		self.id = [num for num in range(N)]
		self.size = [1 for i in range(N)]#每个nodes初始size是1
	
	#判断一个数的根，如果这个数的id是本身则就是根，否则将id作为要找的数继续寻找	
	def root(self,i):
		while i != self.id[i]:
			self.id[i] = self.id[self.id[i]]
			i = self.id[i]
		return i
	
	#将两个数连接起来，先找到两个数的根，如果不同就计算树的size，将小的树作为大的树的child
	def union(self,p,q):
		pid = self.root(p)
		qid = self.root(q)
		if pid != qid:
			if self.size[pid] < self.size[qid]:
				self.id[pid] = qid
				self.size[qid] += self.size[pid]
			else:
				self.id[qid] = pid
				self.size[pid] += self.size[qid]
		
	#判断是否在一棵树上
	def is_connected(self,p,q):
		return self.root(p) == self.root(q)
