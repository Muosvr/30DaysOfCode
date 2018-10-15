import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        queue = []
        result = []

        if not root == None:
            queue.append(root)

        while queue:
            tree = queue.pop(0)
            print(tree.data, end=" ")
            if not tree.left == None:
                queue.append(tree.left)
            if not tree.right == None:
                queue.append(tree.right)
        return result

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
