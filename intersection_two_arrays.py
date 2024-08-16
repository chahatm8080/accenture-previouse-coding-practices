# def intersection(arr1,arr2):
#   i,j=0,0
#   ans=[]
#   while i<len(arr1) and j<len(arr2):
#     if arr1[i]<arr2[j]:
#       i += 1
#     elif arr2[j]<arr1[i]:
#       j += 1
#     else:
#       ans.append(arr1[i])
#       i += 1
#       j += 1
#   return ans

# print(intersection([1,2,2,4],[2,2,3,4]))


#code without using append method in python 
def intersection(arr1,arr2):
  i, j = 0, 0
  k = 0
  ans = [None] * min(len(arr1), len(arr2))
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      i += 1
    elif arr2[j] < arr1[i]:
      j += 1
    else:
      ans[k]=arr1[i]

      i += 1
      j += 1
      k += 1
  return ans[:k]#slice as i am using return the list till last element
print(intersection([1,2,2,1], [2,2,3,4]))