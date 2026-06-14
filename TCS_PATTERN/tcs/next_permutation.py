nums = [1,2,5,4,3]

# Find breakpoint
for right in range(len(nums)-1, 0, -1):
    if nums[right-1] < nums[right]:
        break_point = right-1
        break

# Find next greater element
for right in range(len(nums)-1, break_point, -1):
    if nums[right] > nums[break_point]:
        nums[right], nums[break_point] = nums[break_point], nums[right]
        break
    
left=break_point+1
right=len(nums)-1

while left < right:
    nums[left],nums[right]=nums[right],nums[left]
    left+=1
    right-=1
    
print(nums)