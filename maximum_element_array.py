# using functions
# def maximum(arr):
#   max=arr[0]
#   for num in arr:
#     if num>max:
#       max=num
#   return max
# print(maximum([5,6,7,8,10]))

#without using functions 
# tc and sc will be O(n) and O(1)
arr=[5,6,6,5,54]
max = arr[0]
for num in arr:
  if num>max:
    max=num
print(max)

