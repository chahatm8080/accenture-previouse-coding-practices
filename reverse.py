# string reverse it is 
# def reverse(s):
#   ch=""
#   for i in s:
#     ch=i+ch
#   return ch
# print(reverse("helow"))

def reverse(n):
  reverse=0
  while n!=0:
    r=n%10
    reverse=reverse*10+r
    n=n//10
  return reverse

print(reverse(12345))