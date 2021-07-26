#Linked List Data Structure
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    #insertion beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    #Insert after a node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            return
        new_node = Node(new_data)
        new_data.next = prev_node.next
        prev_node.next = new_node
    #Insert at the end
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def deleteNode(self, position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.nect
            temp = None
            return
        for i in range(position-1):
            temp = temp.next
            if next is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    def search(self, key):
        current = self.head
        while current is not None:
            if currrent.data == key:
                return True
            current = current.next
        return False

    def sortLinkedList(self, head):
        current = head
        index = Node(None)
        if head is None:
            return
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data
                    index = index.next
                current = current.next
        

#Hash Table (Size should not be 2^z)
hashTable = [[],]*10
def checkPrime(n):
    if n==1 or n==0:
        return 0

    for i in range(2, n//2):
        if n%i == 0:
            return 0
    return 1

def getPrime(n):
    if n%2 == 0:
        n = n +1
    while not checkPrime(n):
        n += 2
    return n

def hashFunction(key):
    capacity = getPrime(10)
    return key%capacity

def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    hashTable[hashFunction(key)] = 0

print(hashFunction(23))


#Fibonacci Heap
#Trees of multiple min Heap and max Heap data  structure






