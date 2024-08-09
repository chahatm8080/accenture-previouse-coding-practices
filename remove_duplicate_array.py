def remove_duplicate_array(arr):
  unique_elements=[]
  for elem in arr:
    if elem not in unique_elements:
      unique_elements.append(elem)
  return unique_elements
      

print(remove_duplicate_array([10,10,9,9,8]))
