def maximum_Subarrays(arr):
  n=len(arr)
  res = float('-inf')
  current_Sum=0
  for i in range(0,n):
    current_Sum +=arr[i]
    res=max(current_Sum,res)
    if(current_Sum<0):
      current_Sum=0
  return res
print(maximum_Subarrays([1,-5,4,2,-1]))