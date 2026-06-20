
nums=["a","b","c",'a','b','c','b','b']
l=0
window={}
count=0

for right in range (len(nums)):
    
    if nums[right] in window and window[nums[right]]>=l:
        l=window[nums[right]]+1
        
    window[nums[right]]=right
    count=max(right-l+1,count)
    
print(count)




or 

nums=["a","b","c",'a','b','c','b','b']
seen=set()
left=0
count=0

for right in range(len(add)):
  while nums[right] in seen :
    seen.remove(nums[left])
    left+=1

  seen.add()
  count=max(right-left +1 ,count)


  or 

  arr = ["a", "b", "c", "a", "b", "c", "b", "b"]

window = {}
left = 0
count = 0

for right in range(len(arr)):

    window[arr[right]] = window.get(arr[right], 0) + 1

    while window[arr[right]] > 1:
        window[arr[left]] -= 1

        if window[arr[left]] == 0:
            del window[arr[left]]

        left += 1

    count = max(count, right - left + 1)

print(count)