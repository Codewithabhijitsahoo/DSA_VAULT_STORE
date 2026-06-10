nums = [1, 2, 5, 3, 7, 10, 9, 12]

left=0
right=len(nums)-1

while left < right :
    if nums[left]<nums[left+1]:
         left+=1
    else:
        break
    
while right > 0:
    if nums[right]> nums [right-1]:
        right-=1
    else:
        break

max_=max(nums[left:right])
min_=min(nums[left:right])

while left > 0 and nums[left-1]>min_:
    left-=1

while right < len(nums) and nums[right+1]< max_:
    right+=1
print(nums[left:right+1])
