# array element must be between 1 and n,
# where n is the length of the array.


def find_duplicate(a):
    for i in range(0, len(a)):
        index = abs(a[i])
        if a[index] < 0:
            return index
        else:
            a[index] = a[index] * -1
    return -1


print(find_duplicate([1, 2, 3, 4, 2]))
print(find_duplicate([1, 2, 3, 4, 0]))
