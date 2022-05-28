# def sum_problem(nums, targat):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if targat - nums[i] == nums[j]:
#                 return [i,j]
#     return None
# list=[2,3,14,5,6,7,8,9,1,4,10]
# targart= 18
# print(sum_problem(list, targart))





def two_sum(arr, target):
    dict = {}
    for i, elem in enumerate(arr):
        if elem in dict:
            return[dict[elem], i]
        else:
            dict[target - elem] = i
arr1 = [1,2,3,4,5,6,7,8,9]
target1 = 13
print(two_sum(arr1, target1))