'''
队列Queue满足先进先出原则，因此在dequeue的时候，出来的是最下面的元素，所以除了top我们还需要定义bottom
需要创建node
'''
class Node():
    def __init__(self,cargo,next=None):
        self.cargo = cargo
        self.next = next
        
class Queues():
  def __init__(self):
    self.top = None
    self.bottom = None
  '''
  入队的时候，top不断改变，bottom始终不变
  '''
  def enqueue(self,cargo):
    if self.top is None and self.bottom is None:
      self.top = Node(cargo)
      self.bottom = Node(cargo)
    else:
      self.top = Node(cargo,self.top)
  '''
  出队的时候，返回bottom的值，然后bottom的值变成倒数第二个节点
  '''
  def dequeque(self):
    if self.top is None and self.bottom is None:
      return None
    cargo = self.bottom.cargo
    if self.top == self.bottom:
      self.top = None
      self.bottom = None
    else:
      self.bottom = self.bottom.next
    return cargo
  
  def printqueue(self):
      print('the queue elements are:')
      temp = self.top
      while temp:
          print(temp.cargo,end=' -> ')
          temp = temp.next
