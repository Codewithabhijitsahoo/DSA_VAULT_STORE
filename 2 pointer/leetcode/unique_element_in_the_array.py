nums = [2,2,1]

window={}

left=0

for right in range ( len(nums)):

  window[nums[right]]=window.get(nums[right],0)+1



for right in window :
  if window[right]<2:
    print(window[right])