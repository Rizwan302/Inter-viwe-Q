
def find_duplicate(a):

    map = {}

    for i in a:
        if i in map:
            return i
        else:
            map[i] = 1
    return -1


print(find_duplicate([1, 2, 3, 4, 2]))
print(find_duplicate([1, 2, 3, 4]))