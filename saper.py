from random import *

class Cell:
    def __init__(self, around_mines=0, mine=False, fl_open=True):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open

class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.mines_for_pole = M
        self.pole = [[Cell() for _ in range(self.N)] for _ in range(self.N)]
        self.init() 
        
    def init(self):
        
        while self.mines_for_pole != 0:
            x, y = randint(0, self.N-1), randint(0, self.N-1)
            if self.pole[x][y].mine == False:
                self.pole[x][y].mine = True
                self.mines_for_pole -= 1
                
         
        for i in range(self.N):
            for j in range(self.N):
                if not self.pole[i][j].mine:
                    self.pole[i][j].around_mines = self.getMinesCounter(i, j)

    
    def getMinesCounter(self, i, j):
        n = 0
        for i_offset in range(-1, 2): # Пробегаем оффсет от -1 до +2 от текучего индекса по i
            for j_offset in range(-1, 2): # Пробегаем оффсет от -1 до +2 от текучего индекса по j
                i_index = i + i_offset # Получаем индекс проверяемой клетки по i
                j_index = j + j_offset # Получаем индекс проверяемой клетки по j        
                if any([i_index < 0, i_index >= self.N, j_index < 0, j_index >= self.N]): 
                    continue
                if self.pole[i_index][j_index].mine:
                    n += 1
        return n    
    
    
    def show(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.pole[i][j].fl_open:
                    if self.pole[i][j].mine:
                        print('*', end=' ')
                    else:
                        print(self.pole[i][j].around_mines, end=' ')
                else:
                    print('#', end=' ')
                if j == self.N-1:
                    print('\n')

pole_game = GamePole(10, 12)
pole_game.show()
