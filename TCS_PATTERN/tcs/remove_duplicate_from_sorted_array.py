arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]


#arr = [-3, -3, -1, 0, 0, 5]
left=0
for right in range(len(arr)):
    if arr[right]!=arr[left]:
        left+=1
        arr[left]=arr[right]
        
print(arr[:left+1])