
matrix = [
 [1,2,3,4],
 [5,6,7,8],
 [9,10,11,12],
 [13,14,15,16]
]

top = 0
bottom = len(matrix)-1

left = 0
right = len(matrix[0])-1

ans = []
n=len(matrix[0])


for right in range(n):
    ans.append(matrix[top][right])
    
    
top+=1

for i in range ( top , bottom+1):
    ans.append(matrix[i][right])
right-=1

for j in range(right, left-1,-1):
    ans.append(matrix[bottom][j])
 
bottom-=1
for m in range(bottom,top,-1):
    ans.append(matrix[m][left])
    
for j in range(left,right+1):
    ans.append(matrix[top][j])
print(ans)