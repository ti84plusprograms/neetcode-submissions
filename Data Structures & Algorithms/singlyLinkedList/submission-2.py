class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.value
            i += 1
            curr = curr.next
        
        return -1
        
    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            dummy = Node(val)
            dummy.next = self.head
            self.head = dummy
        

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            curr = self.head
            while curr and curr.next:
                curr = curr.next
            curr.next = Node(val)
        

    def remove(self, index: int) -> bool:
        # if empty
        if not self.head:
            return False 
        # if one node
        if not self.head.next:
            if index == 0:
                self.head = None
                return True
            else:
                return False

        curr = self.head
        i = 0
        while curr and curr.next:
            if index == 0:
                self.head = self.head.next
                return True
            elif index == i + 1:
                curr.next = curr.next.next
                return True
            i+=1
            curr = curr.next
        
        return False
        

    def getValues(self) -> List[int]:
        curr = self.head
        values = []
        while curr:
            values.append(curr.value)
            curr = curr.next
        return values
            
        
