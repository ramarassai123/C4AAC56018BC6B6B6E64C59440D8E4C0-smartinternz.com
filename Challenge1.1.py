def recur_factorial(n):
  if n==1:
    return n
  else:
    return n*recur_factorial(n-1)
num=int(input("Enter the value:"))
if num<0:
    print("Sorry,factorial does not exit for negative number")
elif num==0:
    print("the factorial of 0 is 1")
else:
    print("'the Factorial of'is=",recur_factorial(num))