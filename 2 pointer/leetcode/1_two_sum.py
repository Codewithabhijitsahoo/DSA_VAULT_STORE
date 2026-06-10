nums = [2, 7, 11, 15]
target = 9

left=0
right=len(nums)

while left < right :
  sum_=nums[left]+nums[right]
  if sum_==target:
    print("meet reqw condition ")
    left+=1
    right-=1
  elif sum_ < target :
    left+=1
  else:
    right-=1