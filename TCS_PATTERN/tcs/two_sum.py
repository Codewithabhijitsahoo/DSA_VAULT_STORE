nums = [2,7,11,15]
target = 9

left=0
right=len(nums)-1

while left < right :
  current_sum=nums[left]+nums[right]

  if current_sum==target:
    print("found")
    right-=1
    left+=1
  elif current_sum< target:
    left+=1
  else:
    right-=1