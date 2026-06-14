arr = [-2,1,-3,4,-1,2,1,-5,4]

best_ending=arr[0]
ans=arr[0]

for right in range(1,len(arr)):
    n1=best_ending+arr[right]
    n2=arr[right]
    
    best_ending=max(n1,n2)
    ans=max(ans,best_ending)
    
print(ans)