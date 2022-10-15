class StackObj:
    
    def __init__(self, data):
        self.__data = data
        self.__next = None
        
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, value):
        if type(value) is StackObj or value is None: 
            self.__next = value
    
    @property
    def data(self):
        return self.__data 
    @data.setter
    def data (self, value):
        self.__data = value
    
    
class Stack:
    def __init__(self):
        self.top = None
        self.last  = None
        
    def push(self, obj):
        if not self.top:
            self.top = obj
        else:
            self.last.next = obj    
        self.last = obj
    
    def pop(self):
        if self.top is not None and self.top != self.last:
            item = self.top
            while self.last != item:
                link = item
                item = item.next
            link.next = None
            res = self.last.data
            self.last = link
            return res
        elif self.head is not None and self.last == self.top:
            res = self.top.data
            self.last = None
            self.top = None
            return res
    
    def get_data(self):
        l = []
        nex = self.top
        while nex:
            l += [nex.data]
            nex = nex.next
        return l

st = Stack()
a = StackObj("obj1")
b = StackObj("obj2")
c = StackObj("obj3")
st.push(a)
st.push(b)
st.push(c)
res = st.get_data()
print(res)
print(a.next)
print(b.next)
print(c.next)
print()
print(a)
print(b)
print(c)
print()
st.pop()
res = st.get_data()
print(res)
print(a.next)
print(b.next)
print(c.next)
