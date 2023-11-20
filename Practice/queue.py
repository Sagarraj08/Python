class queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self,item):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Empty queue")
    def is_empty(self):
        return len(self.items)==0
    
qu=queue()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
qu.enqueue(40)
qu.enqueue(50)
print(qu.items)
qu.dequeue(20)
print(qu.items)
qu.dequeue(22)
print(qu.items)
