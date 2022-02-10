def sum_problem(nums, targat):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if targat - nums[i] == nums[j]:
                return [i,j]
    return None
list=[2,3,14,5,6,7,8,9,1,4,10]
targart= 18
print(sum_problem(list, targart))