a=0
b=1
n=int(input("Enter the number "))
for i in range(n):
    f=a+b
    a=b
    b=f
    print(str(f)+" ")

