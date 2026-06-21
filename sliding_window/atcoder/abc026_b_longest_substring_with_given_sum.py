target = 7
nums = [2,3,1,2,4,3]

window = 0
count = 0
left = 0

for right in range(len(nums)):
    window += nums[right]

    # shrink only when sum > target
    while window > target:
        window -= nums[left]
        left += 1

    # check exact match
    if window == target:
        count = max(count, right - left + 1)

print(count)

or 

arr = [4, 1, 1, 1, 2, 3, 5]
k = 5

left=0
count=0
summ=0
for right in range(len(arr)):
    summ+=arr[right]
    
    if summ==k:
        
        count=max(count,right-left+1)
        
        summ=arr[right]
        left=right
print(count)
