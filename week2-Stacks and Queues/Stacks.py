‘’‘
栈（stacks）就像书堆，后进的数据先出来
为了构建stacks需要链表结构（linked list）
为了构建链表结构需要节点（node）
节点是一个这样的结构，拥有值与指针
节点的指针指向下一个节点的值，从而构成了链表
入栈（push）新节点的指针指向旧的节点的值
出栈（pop）最上节点变成下一个节点即可
’‘’
'''
第一个节点指针是none
'''
class Node():
    def __init__(self,cargo,next=None):
        self.cargo = cargo
        self.next = next
    '''
    作用能使print(node)输出值
    '''
    def __str__(self):
        return self.cargo


node1 = Node('to')
node2 = Node('be')
node3 = Node('or')
node1.next = node2
node2.next = node3
def println(node):
    while node:
        print (node)
        node = node.next
println(node1)
print(node1.next)
'''
生成一个最上面的元素
'''
class Stack():
    def __init__(self):
        self.top = None

    '''
    入栈，将新建的节点作为最上面的元素
    '''
    def push(self,cargo): 
        if self.top is None:
            self.top = Node(cargo) 
        else:
            self.top = Node(cargo,self.top)


    '''
    出栈，将最上面的元素变成下面一个元素,返回值是pop的元素内容
    '''
    def pop(self):                    
        if self.top is None:
            return None
        cargo = self.top.cargo
        self.top = self.top.next
        return cargo
    '''
    返回最顶层的元素
    '''
    def peek(self):
        return self.top.cargo if self.top is not None else None


    def isempty(self):
        return self.peek() is None

    def size(self):
        temp =self.top
        count = 0
        while temp is not None:
            count+=1
            temp = temp.next
        return count

    def printstack(self):
        print('the stack elements are:')
        temp = self.top
        while temp:
            print(temp.cargo,end=' -> ')
            temp = temp.next


if __name__ == "__main__":
    stack = Stack()
    stack1 = stack.push('dog')
    stack1 = stack.push(2)
    print (stack.peek()) 
    print(stack.printstack())
    stack.pop()
    print(stack.peek())

'''
利用stack定义函数，可以将输入的字符串逆序输出
'''
def revstr(string):
    rever =''
    stack = Stack()
    for i in string:
        stack.push(i)
    while not stack.isempty():
        rever += stack.pop()
    return rever
    
print(revstr('apple'))
