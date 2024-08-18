# def occurence(arr):
#   count={}
#   for elem in arr:
#     if elem in count:
#       count[elem]+=1
#     else:
#       count[elem]=1
#   return count
# print(occurence([10,10,2,2,1,3]))# tc=O(n) and sc=O(n)

# Counting occurence of each element in an array
def count_occurrences(arr):
    arr.sort()  
    n = len(arr)
    
    if n == 0:
        return
    
    current = arr[0]
    count = 1
    #[1,2,2,3,10,10]
    for i in range(1, n):
        if arr[i] == current:
            count += 1
        else:
            print(f"{current} occurs {count} time")
            current = arr[i]
            count = 1
    
    print(f"{current} occurs {count} time")# f is formatted string literal which is used to define the variable 

# Example usage
count_occurrences([10, 10, 2, 2, 1, 3])
