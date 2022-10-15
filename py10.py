n = int(input())
k = int(input())

lst = []
for i in range(k):
    temp = []
    curr_i = n**i
    for j in range(len(lst)):
        temp += [lst[j] + curr_i]
    temp += [curr_i]
    lst.extend(temp)

lst.sort()
print(lst)
print(lst[k-1])
        
