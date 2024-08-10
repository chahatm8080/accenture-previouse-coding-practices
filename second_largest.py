def second_largest(arr):
  largest = second_largest = float('-inf')  
  for num in arr:
    if num>largest:
      second_largest = largest
      largest=num
    elif num>second_largest and num!=largest:
      second_largest=num
  return second_largest
print(second_largest([1,2,3,4,5]))