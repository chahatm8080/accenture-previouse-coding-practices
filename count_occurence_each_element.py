def occurence(arr):
  count={}
  for elem in arr:
    if elem in count:
      count[elem]+=1
    else:
      count[elem]=1
  return count
print(occurence([10,10,2,2,1,3]))