
arr = [3, 2, 2, 3, 4, 3]
target = 3
left=0

for right in range(len(arr)):
    
    if arr[right]!=target:
        arr[left]=arr[right]
        left+=1
print(arr[:left])