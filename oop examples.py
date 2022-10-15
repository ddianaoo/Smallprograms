import sys

# здесь объявляйте класс
class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = int(year)
        
    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))
        
    def __eq__(self, other):
        return hash(self) == hash(other)
        
        
# считывание списка из входного потока
#lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in не менять!
lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]
# здесь продолжайте программу (используйте список строк lst_in)
lst_bs = []
for line in lst_in:
    name, author, year = line.split('; ')
    lst_bs += [BookStudy(name, author, year)]
    
#unique_books = len(set(hash(i) for i in lst_bs))
print(*lst_bs, sep='\n')
print()
print(*set(lst_bs), sep='\n')
print(unique_books)
