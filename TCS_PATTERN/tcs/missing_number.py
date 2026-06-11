arr = [1, 2, 4, 5]

n = len(arr) + 1

expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)

missing_number = expected_sum - actual_sum

print(missing_number)