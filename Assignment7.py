items = ["samsung","mobile","like","ice","icecream","sam","sung","cream","man", "go", "mango","i"]
str2=""
str = input("Enter the string : ") 
length = len(str)
index =0
for i in range(0,len(str)):
  subs = str[0:index+1]
  if(subs in items):
    str2=str2+" "+subs
    str=str.replace(subs,"",1)
    index=0
  else:
    index+=1
if(len(str)!=0):
   print("Cannot separate !!")
else:
  print(str2)
