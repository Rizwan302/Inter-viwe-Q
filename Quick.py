def Quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a.pop()
    Greater = []
    Lass = []
    for i in a:
        if  i < pivot:
            Greater.append(i)
        else:
            Lass.append(i)
    return Quick_sort(Greater) + [pivot] + Quick_sort(Lass)
list=[9,8,2,1,7,4,5,3,6]
print(Quick_sort(list))