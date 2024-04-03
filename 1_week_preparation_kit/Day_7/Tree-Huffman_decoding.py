"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-tree-huffman-decoding/problem
"""

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    # Enter Your Code Here
    
    data=[]
    node = root
    next_node=None
    
    for code in s:

        if code == "0":
            next_node=node.left

        elif code == "1":
            next_node=node.right
            
        if not next_node.left and not next_node.right:
            data.append(next_node.data)
            node=root

        else:
            node=next_node
            
    decoded = "".join(data)
    
    print(decoded)