# string reverse it is 
def reverse(s):
  ch=""
  for i in s:
    ch=i+ch
  return ch
print(reverse("helow"))