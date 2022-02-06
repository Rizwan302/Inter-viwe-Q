
def find_duplicate(a):
    a = sorted(a)
    for i in range(0, len(a)-1):
        if a[i] == a[i+1]:
            return a[i]
    return -1


print(find_duplicate([1, 2, 3, 4, 2]))
print(find_duplicate([1, 2, 3, 4]))
