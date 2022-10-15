class Matrix:
    def ___init__(self, rows_or_list, cols=0, fill_value=0):
        if type(rows_or_list) == list:
            self._rows = len(rows_or_list)
            self._cols = len(rows_or_list[0])
            if not all(len(r) == self._cols for r in rows_or_list) or \
               not all(self.__is_digit(x) for row in rows_or_list for x in row):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')

            self._lst = rows_or_list
        else:
            if type(rows_or_list) != int or type(cols) != int or type(fill_value) not in (int, float):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

            self._rows = rows_or_list
            self._cols = cols
            self._lst = [[fill_value for j in range(cols)] for i in range(rows_or_list)]

        @staticmethod
        def __is_digit(x):
            return type(x) in (int, float)

        def check_index(self, indexes):
        if 0 <= indexes[0] < self.rows and 0 <= indexes[1] < self.cols:
            return True
        raise IndexError('недопустимые значения индексов')

    
        def __getitem__(self, keys):
            self.check_index(keys)
            return self.lst[keys[0]][keys[1]]

        def __setitem__(self, keys, value):
            self.check_index(keys)
            if not self.__is_digit(value):
                raise TypeError('значения матрицы должны быть числами')
            self.lst[keys[0]][keys[1]] = value

        def __check_dimensions(self, m):
            if m1.rows != m2.rows or m1.cols != m2.cols:
            raise ValueError('операции возможны только с матрицами равных размеров')

        

        def __add__(self, other):
            if type(other) == type(self):
                self.__check_dimensions(other)
                return Martix([[self.lst[i][j] + m2.lst[i][j] for j in range(self.cols)] for i in range(self.rows)])
                
            else:
                self.__is_digit(other)
                return Martix([[self.lst[i][j] + other for j in range(self.cols)] for i in range(self.rows)])
            






    
