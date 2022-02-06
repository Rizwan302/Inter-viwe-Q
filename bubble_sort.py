from turtle import left, right

 
def Bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list
list = [4,7,2,1,6,3,5]
p = Bubble_sort(list)
print(p)
 
           
                        
def Merge(array):
    if len(array) < 2:
        return array
    mid= len(array) // 2
    left = Merge(array[:mid])
    right = Merge(array[mid:])
    return Merge_sort(left, right)
    
def Merge_sort(left,right):
    result=[]
    i, j =0,0
    while i<len(left) or j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or  j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result 

list=[2,1,6,2,4,9,5,7]
print(Merge(list))