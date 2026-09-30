a = float(input("enter the first number"))
b = input("enter opreator(+,_,/,*):")
c = float(input("enter the second number"))
if b =="+":
    result = a+c
elif b =="-":
    result = a-c
elif b =="*":
    result = a*c
elif b =="/":
    if c == 0:
      result ="we cannot divide by the zero" 
    else:
     result  = a/c
else :
   result = "invalid b"
print("result:",result)