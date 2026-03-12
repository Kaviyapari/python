def sq():
    s=int(input("Enter the sides of Square:"))
    print("Area of the Square is ",s*s)
def rect(l,b):
    print("Area of the Rectangle is ",l*b)
def tri():
    base=int(input("Enter Base: "))
    ht=int(input("Enter ht: "))
    return 0.5*base*ht
def cir(r):
    return 3.14*r*r
print("1.Square")
print("2.Rectangle")
print("3.Triangle")
print("4.Circle")
print("**********")
ch=int(input("Enter your Choice of Shape: "))
if(ch==1):
    sq()
elif(ch==2):
    l=int(input("Enter your Length: "))
    b=int(input("Enter your Breadth: "))
    rect(l,b)
elif(ch==3):
    x=tri()
    print("Area of Triangle: ",x)
elif(ch==4):
    r=int(input("Enter Radius: "))
    y=cir(r)
    print("Area of Circle is : ",y)
else:
    print("Invalid Input")