def findPermutation(p, q):
    lenn = len(p)
    lst = [0]*lenn
    for i in range(1, lenn+1):
        q_val = q[i-1]
        p_ind = p.index(q_val)
        lst[i-1] = p_ind + i
    return lst


p = [3, 4, 1, 2, 5]
q = [4, 5, 2, 3, 1]
print(findPermutation(p, q))
