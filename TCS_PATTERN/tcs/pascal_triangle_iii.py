
result=[]
k=1
while k<=5:
    n=k-1
    ans = 1
    ans1=[1]
    for right in range(n):
        ans=ans*(n-right)
        ans=ans//(right+1)
        ans1.append(ans)
    result.append(ans1)
    k+=1
print(result)