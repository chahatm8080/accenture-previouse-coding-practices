def min_chocolates(arr):
    arr.sort()
    min_chocolates_needed = float('inf')
    for i in range(len(arr)- 1):
      chocolates_needed = arr[i + 1]- arr[i]
      min_chocolates_needed = min(min_chocolates_needed, chocolates_needed)
    return min_chocolates_needed
arr1 = [10, 4, 12, 3, 1]
output1 = min_chocolates(arr1)
print(output1)