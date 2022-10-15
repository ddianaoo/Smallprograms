class Matrix:
    def __init__(self, *args):
        if len(args) == 3:
            self.rows = args[0]
            self.cols = args[1]
            self.fill_value = args[2]
            self.lst = [[self.fill_value for j in range(self.cols)] for i in range(self.rows)]
        elif len(args) == 1:
            self.check_matrix(args[0])
            self.lst = args[0]
            self.rows = len(self.lst)
            self.cols = len(self.lst[0])
            
            
    
    def check_matrix(self, l):
        lens = [len(i) for i in l]
        t = [[type(l[i][j]) in (int, float) for j in range(len(l[i]))]for i in range(len(l))]
        check = all([i for j in t for i in j])
        if max(lens) != min(lens) or check == False:
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')
        
            
        
    def __setattr__(self, key, value):
        if (key == 'rows' and type(value) != int) or (key == 'cols' and type(value) != int) or (key == 'fill_value' and type(value) not in (int, float)):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
        else:
            object.__setattr__(self, key, value)


    def check_index(self, indexes):
        if 0 <= indexes[0] < self.rows and 0 <= indexes[1] < self.cols:
            return True
        raise IndexError('недопустимые значения индексов')

    
    def __getitem__(self, keys):
        self.check_index(keys)
        return self.lst[keys[0]][keys[1]]

    def __setitem__(self, keys, value):
        self.check_index(keys)
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        self.lst[keys[0]][keys[1]] = value

    @staticmethod    
    def check_size(m1, m2):
        if m1.rows != m2.rows or m1.cols != m2.cols:
            raise ValueError('операции возможны только с матрицами равных размеров')

            
    #operations
    def __add__(self, other):
        if type(other) in (int, float):
            m2 = type(self)(self.rows, self.cols, other)   
        elif type(other) == type(self):
            m2 = other
            
        type(self).check_size(self, m2)
        last = [[(self.lst[i][j] + m2.lst[i][j]) for j in range(self.cols)] for i in range(self.rows)]
        print(last)
        return type(self)(last)    
    

    def __sub__(self, other):
        if type(other) in (int, float):
            m2 = type(self)(self.rows, self.cols, other)   
        elif type(other) == type(self):
            m2 = other
            
        type(self).check_size(self, m2)
        last = [[(self.lst[i][j] - m2.lst[i][j]) for j in range(self.cols)] for i in range(self.rows)]
        return type(self)(last)    
    
    




        
l = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 3]]
        
l2 = [[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]

m1 = Matrix(l)        
m2 = Matrix(l2)
m3 = m1 + 1
#print()
print(m3.__dict__)
