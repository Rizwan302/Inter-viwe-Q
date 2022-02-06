
def find_duplicate(a):
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return a[i]
    return -1


print(find_duplicate([1, 2, 3, 4, 2]))
print(find_duplicate([1, 2, 3, 4]))
