

def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        # print('i', i)
        j = i-1
        # print('j', j)
        while j >=0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
        # print(nums)
    return nums   