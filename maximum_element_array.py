def maximum(arr):
  max=arr[0]
  for num in arr:
    if num>max:
      max=num
  return max
print(maximum([5,6,7,8,10]))