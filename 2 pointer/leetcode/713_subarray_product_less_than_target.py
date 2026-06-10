nums = [10, 5, 2, 6]
k = 100

winodw=1
count=0
left=0

for right in range (len(nums)):
  window*=nums[right]

  while window >= target:
    window=window//nums[left]
    left+=1

  cont+=right-left+1