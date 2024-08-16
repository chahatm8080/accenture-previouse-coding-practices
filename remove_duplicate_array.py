# def remove_duplicate_array(arr):
#   unique_elements=[] 
#   for elem in arr:# tc O(n)
#     if elem not in unique_elements:
#       unique_elements.append(elem)
#   return unique_elements
# print(remove_duplicate_array([10,10,9,9,8]))#time = O(n) Space = O(n)  map using



#Optimized code without using extra space now i am trying to make it big of O(1)

def rm_duplicate(arr):
  arr.sort()
  index=0
  for i in range(1,len(arr)):
    if arr[i] != arr[index]:
      index +=1
      arr[index]=arr[i]
  return arr[:index+1]
print(rm_duplicate([10,10,9,9,8,11,11]))