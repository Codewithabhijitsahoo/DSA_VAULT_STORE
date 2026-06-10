arr = [10, 5, 2, 7, 1, 9]
k = 15

window=0
left=0
length=0
mk=[]
for right in range(len(arr)):
    window+=arr[right]
    
    while window>=k:
        if window==k:
            mk.append(arr[left:right+1])
            length=max(length,right-left+1)
        window-=arr[left]
        left+=1
        
print(length)
print(mk)
        