n = 12345
count = 0

while n>0:
    k=n%10
    n=n//10
    if k % 2 !=0:
        count+=1
    
print(count)