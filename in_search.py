# n = int(input("Enter number of elements in the list : "))
# print('try')
# def sss(n):
#   listA = []
      
#   # iterating till the range
#   for i in range(0, n):
#     print("Enter element No-{}: ".format(i+1))
#     elm = int(input('num'))
#     a = elm * elm
#     listA.append(a) # adding the element
#   print("The entered list is: \n",sum(listA))   
# sss(n)     

# def create_sequence_num(n):
#     terms = 1
#     while n > 1:
#         if n % 2 == 0:
#             n = n / 2
#         else:
#             n = 3 * n + 1
#         terms += 1
#     return terms
# def Collatz_starting_num():
#     temp = 0
#     i = 1
#     while i < 10000:
#         s = create_sequence_num(i)
#         if s > temp:
#             temp = s
#             value = i
#         i += 1
#     return value
# print(Collatz_starting_num())








class Node:
      def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)


#   1
#  2 3 has 6 on left
# 4 5
#--------------------
# 4 5 6
#--------------------
# BFS = 123456
def bfs(root: Node):
  if root is None:
    return
  queue = [root]
  
  queue.append(root)
  while len(queue) > 0:
    print(queue[0].data)
    cur_node = queue.pop(0)
    
    if cur_node.left is not None:
      queue.append(cur_node.left)
    
    if cur_node.right is not None:
      queue.append(cur_node.right)


bfs(root)



def dfs(root, visited):
  if root:
    visited = dfs(root.left, visited)
    visited.append(root.data)
    visited = dfs(root.right, visited)
  return visited

print(dfs(root, []))
        
    




    






# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.left = None
#     self.right = None
          
# class Tree:
#   def __init__(self,root):
#  		self.root=Node(root)
   

# tree=Tree(3)
# tree.root.left=Node(9)
# tree.root.right=Node(20)
# tree.root.right.left=Node(15)
# tree.root.right.right=Node(7)
# def in_order(root, stack):
#   if root:
#     stack=in_order(root.left, stack)
#     stack.append(root.data)
#     stack=in_order(root.right, stack)
#   return stack

# def preorder(root, visited):
#   if root:
#     visited.append(root.data)
#     visited = preorder(root.left,visited)
#     visited = preorder(root.right,visited)
#   return visited

# def postorder(root, visited):
#   if root:
#     visited = postorder(root.left, visited)
#     visited = postorder(root.right, visited)
#     visited.append(root.data)
#   return visited
        
     
     
     

# print(in_order(tree.root,[]))
# print(preorder(tree.root,[]))
# print(postorder(tree.root,[]))

    
    
    

