class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left 

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr!=self.right and index > 0:
            curr = curr.next
            index -= 1
        if index == 0 and curr != self.right:
            return curr.val
        else:
            return -1
        
    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        temp = self.left.next
        node.next = temp
        temp.prev = node
        node.prev = self.left
        self.left.next = node

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        temp = self.right.prev
        node.next = self.right
        self.right.prev = node
        node.prev = temp
        temp.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        #need to know the length
        #two conditions for that
        node = ListNode(val)
        curr = self.left.next
        while curr != self.right and index>0:
            curr = curr.next
            index -= 1
        if index == 0:
            temp = curr.prev
            node.next = curr
            temp.next = node
            node.prev = temp
            curr.prev = node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr != self.right and index > 0:
            curr = curr.next
            index -= 1
        if index == 0 and curr != self.right:
            temp = curr.prev
            temp2 = curr.next
            temp.next = temp2
            temp2.prev = temp

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)