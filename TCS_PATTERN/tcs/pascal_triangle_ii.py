row = 7-1

ans=1
k=[1]
for right in range(4):
    ans=ans*(row-right)
    ans=ans//(right+1)
    k.append(ans)
    
print(k)