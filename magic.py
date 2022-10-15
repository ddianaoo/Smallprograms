from random import randint

class Cell:
    def __init__(self):
        self.value = 0
        
    def __bool__(self):
        return True if self.value == 0 else False


    
class TicTacToe:
    
    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2 
    
    def __init__(self):
        self.pole = [ [Cell() for j in range(3)]  for i in range(3)]
    
    def init(self):
        self.pole = [ [Cell() for j in range(3)]  for i in range(3)]
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False
    
    @staticmethod
    def check_index(items):
        if not all([i in [0, 1, 2] for i in items]):
            raise IndexError('некорректно указанные индексы')
            
    def __getitem__(self, items):
        self.check_index(items)
        return self.pole[items[0]][items[1]].value
    
    def __setitem__(self, items, value):
        self.check_index(items)
        self.pole[items[0]][items[1]].value = value
        
        
    def show(self):
        for i in self.pole:
            print([j.value for j in i], sep='\n')
        
    def human_go(self):
        x, y = input('Please, enter coordinations of choosen cell: ').split()
        self.__setitem__((int(x), int(y)), self.HUMAN_X)


    def computer_go(self):
        while True:
            x, y = randint(0,2), randint(0,2)
            if self.pole[x][y].value == self.FREE_CELL:
                self.__setitem__((x, y), self.COMPUTER_O)
                break
                
            
    
    def __bool__(self):
        res = any([[j.value == self.FREE_CELL for j in i] for i in self.pole])
        d11 = all([self.pole[i][i].value == self.HUMAN_X for i in range(len(self.pole))])
        d12 = all([self.pole[i][-1-i].value == self.HUMAN_X for i in range(len(self.pole))])
        
        d21 = all([self.pole[i][i].value == self.COMPUTER_O for i in range(len(self.pole))])
        d22 = all([self.pole[i][-1-i].value == self.COMPUTER_O for i in range(len(self.pole))])

        if d11 or d12:
            self.is_human_win = True
        elif d21 or d22:
            self.is_computer_win = True
        else:
            self.is_draw = True 
        return True if res and all([i == False for i in [d11, d12, d21, d22]]) else False


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()
    print()
    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
