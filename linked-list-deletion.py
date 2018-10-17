class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
    #Write your code here
        memory = []
        if head.data != None:
            memory.append(head.data)
        if head.next != None:
            current = head.next
            last = head
            while current:
                print("Current data", current.data)
                if current.data in memory:
                    print("Found duplicate:{}".format(current.data))
                    last.next = last.next.next
                    current = last.next
                else:
                    memory.append(current.data)
                    last = current
                    current = current.next

            print('Memory: {}'.format(memory))
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);
