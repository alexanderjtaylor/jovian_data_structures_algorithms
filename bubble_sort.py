
def bubble_sort(nums):
    # Create a copy of the list, to avoid changing it
    nums = list(nums)
   # print('bubble_sort', nums)
    
    # 4. Repeat the process n-1 times
    for j in range(len(nums) - 1):
      # print('iteration', j)
        # 1. Iterate over the array (except last element)
        for i in range(len(nums) - 1):
          # print('i', i, nums[i], nums[i+1])
            # 2. Compare the number with  
            if nums[i] > nums[i+1]:
                
                # 3. Swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    # Return the sorted list
    return nums