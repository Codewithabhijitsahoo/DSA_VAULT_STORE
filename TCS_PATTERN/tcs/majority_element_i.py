arr = [2,2,1,1,1,2,2]

candidiate=0
count=0 # 1 

for right in range(len(arr)):
    
    if count==0:
        candidate=arr[right]
        
    if arr[right]==candidate:
        count+=1
    else:
        count-=1
print(candidate)