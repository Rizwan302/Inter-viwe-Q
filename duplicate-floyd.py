
def find_duplicate(l):

    if l.__len__() <= 1:
        return -1
    else:
        p = l[0]
        q = l[l[0]]

        while p != q:
            p = l[p]
            q = l[l[q]]

        q = 0
        while p != q:
            p = l[p]
            q = l[q]

        return p


print(find_duplicate([1, 2, 3, 4, 2]))
print(find_duplicate([1, 4, 3, 4, 3]))
print(find_duplicate([0, 1, 0, 3, 4]))
