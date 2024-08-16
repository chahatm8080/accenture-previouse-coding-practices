# def missing(arr):
#   n=len(arr)+1
#   total_sum=n*(n+1)//2
#   actual_sum=sum(arr)
#   return total_sum-actual_sum


# print(missing([1,2,3,5,6]))

# Time complexity and space complexity will be O(n) and O(1)

def missing_num(arr):
  n=len(arr)+1
  total_sum=n*(n+1)//2
  actual_sum=sum(arr)
  return total_sum-actual_sum

print(missing_num([3,5,4,1,2]))