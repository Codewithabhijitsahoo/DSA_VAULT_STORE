n = list(str(12345))

k=[]

for right in range(len(n)-1,-1,-1):
    k.append(n[right])
    
n=int("".join(k))
print(type(n))


or 

n = 12345
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print(rev)
