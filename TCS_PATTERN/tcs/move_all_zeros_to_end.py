arr = [1, 0, 2, 0, 3, 4, 0]
left=0
right=len(arr)-1

while left<right:
    if arr[left]==0:
        arr[right],arr[left]=arr[left],arr[right]
        right-=1
    left+=1
print(arr)
    