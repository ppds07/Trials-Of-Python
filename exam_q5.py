def alter(s, t):
   i = j = 0
   result = ""
   while i < len(s) and j < len(t):
      result=result + s[i] + t[j]
      i=i+1
      j=j+1
   while i < len(s):
      result =result+s[i]
      i=i+1
   while j < len(t):
      result=result+t[j]
      j=j+1
   return result
s=str(input("Enter first word: "))
t=str(input("Enter secong word: "))
print(alter(s, t))