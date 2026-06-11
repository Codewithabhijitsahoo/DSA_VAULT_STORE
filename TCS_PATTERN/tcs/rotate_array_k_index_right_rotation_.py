arr = [1, 2, 3, 4, 5, 6, 7]# 1 2  3 4 5 6 6
                           # 1 2  3 4 5 5 6
k = 3                      # 1 2  3 4 4 5 6
n = len(arr)               # 1 2  3 3 4 5 6
                           # 1 2  2 3 4 5 6
count = 0                  # 6 1 2 3 4 5  1

while count < k:
    first_element = arr[0]

    for i in range(n-1,-1,-1):
        arr[i] = arr[i - 1]

    arr[n - 1] = first_element

    count += 1

print(arr)