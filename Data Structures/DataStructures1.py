def create_stack():
    stack = []
    return stack
def check_empty(stack):
    return len(stack) == 0
def push(stack, item):
    stack.append(item)
def pop(stack):
    if check_empty(stack):
        return None
    return stack.pop()

#Simple Queue: Disadvantage memeory 
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        #Built-In reindexing
        return self.queue.pop(0)
    def display(self):
        print(self.queue)
    def size(self):
        return len(self.queue)

class MyCircularQueue:
    def __init__(self,  k):
        self.k = k
        #Dynamic Size initialization
        self.queue = [None]*k
        self.head = self.tail = -1

    def enqueue(self, item):
        if ((self.tail + 1)%self.k == self.head):
            print("Full!")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item
        else:
            self.tail = (self.tail + 1)%self.k
            self.queue[self.tail] = item

    def dequeue(self):
        if (self.head == -1):
            print("Empty!")
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.haed+1)%self.k
            return temp

#Heap Implementation of the priority queueu
def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l<n and arr[i] < arr[l]:
        largest = l
    if r<n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:       
        array.append(newNum)
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)

def deleteNode(array, num):
    size = len(array)
    i=0
    for i in range(0, size):
        if num == array[i]:
            break
    array[i], array[size-1] = array[size-1], array[i]
    array.remove(size-1)

    for i in (range(len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)

class Dequeue:
    """Python Built-In reindexing it will work"""
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addRear(self, item):
        self.items.append(item)
    def addFront(self, item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop(0)
    def removeRear(self):
        return self.items.pop()
    def size(self):
        return len(self.items)




