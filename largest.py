def largest(arr):
  n=len(arr)
  large=arr[0]
  for i in range(1,n):
    if arr[i]>large:
      large=arr[i]
  return large

print(largest([10,202,2,3,4,5]))