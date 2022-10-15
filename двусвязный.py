class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail  = None
            
    def add_obj(self, obj):
        if not self.head:
            self.head = obj
        else:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)    
        self.tail = obj
        
    def remove_obj(self):
        if self.head is not None and self.tail != self.head:
            s = self.tail.get_prev()
            s.set_next(None)
            self.tail.set_prev(None)
            self.tail = s
            s = None
        elif self.head is not None and self.tail == self.head:
            self.head = None
            self.tail = None
            
    def get_data(self):
        l = []
        nex = self.head
        while nex:
            l += [nex.get_data()]
            nex = nex.get_next()
        return l

class ObjList:
    
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None   
        
    def set_next(self, obj):
        self.__next = obj
    
    def set_prev(self, obj):
        self.__prev = obj
    
    def get_next(self):
        return self.__next
    
    def get_prev(self):
        return self.__prev
    
    def set_data(self, data):
        self.__data = data
    
    def get_data(self):
        return self.__data


ls = LinkedList()
ls.add_obj(ObjList("данные 1"))
#ls.add_obj(ObjList("данные 2"))
print(ls.get_data())
ls.remove_obj()
print(ls.get_data())
