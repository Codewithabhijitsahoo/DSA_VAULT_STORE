arr = [1, 3, 5, 8, 10]
k = 2

left=0
right=1
count=0
while right < len(arr)  :
    diff=arr[right]-arr[left]
    
    if diff < k :
        right+=1
    elif diff > k:
        left+=1
    else:
        count+=1
        right+=1
        left+=1
        
print(count)
        
