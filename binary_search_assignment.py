
#function finds the number of times an ordered list in increasing order is rotated (number at the end of the list is moved to the beginning of list)
def count_rotations_binary(nums):
    lo = 0
    hi = len(nums) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid > 0 and mid_number < nums[mid - 1]:
            return mid
        
        elif mid_number < hi:
            hi = mid - 1  
        
        else:
            lo = mid + 1
    
    return 0