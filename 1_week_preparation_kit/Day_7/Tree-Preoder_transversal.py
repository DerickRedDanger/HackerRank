"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-tree-preorder-traversal/problem
"""

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    # Write your code here
    
    Order=[]
    stack=[root]
    
    # While there are elements in the stack
    while len(stack) >= 1:
        node=stack.pop()
        
        
        Order.append(str(node.info))
        
        # Since we want to process the lowest element first, we will add the highest first.
        if node.right:
            stack.append(node.right)
        
        # and then the lowest
        if node.left:
            stack.append(node.left)
            
    result=" ".join(Order)
    print(result)