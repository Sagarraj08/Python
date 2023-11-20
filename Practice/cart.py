class Cart:
    def __init__(self):
        self.items=[]
    def add(self,itemname,qty):
        item=(itemname,qty)
        self.items.append(item)
    def remove(self,itemname):
        for item in self.items:
            if item[0]==itemname:
                self.items.remove(item)
                break
    def total(self):
        total=0
        for item in self.items:
            total=total+item[1]
        return total
shop=Cart()
shop.add('biscuit',2)
shop.add("milk",2)
shop.add("maggie",3)
print(shop.items)
shop.remove("biscuit")
print(shop.items)
print(shop.total())

