a=int(input("Enter the number1:"))
b=int(input("Enter the number2:"))
c=int(input("Enter the number3:"))
a1=[int(i) for i in str(a)]
b1=[int(i) for i in str(b)]
c1=[int(i) for i in str(c)]
large=max(a1)+max(b1)+max(c1)
small=min(a1)+min(b1)+min(c1)
print("Key is",large*small)
                        


 