name=['Anu','Raj','Rosy','Varun']
age=[24,30,28,27,29]
city=['Pondy','Mahe','Yanam','Karaikal','Cuddalore']
b=list(zip(age,name,city))
c=sorted(b)
s=1
for i in c:
    print("{}.{} age is {} - Living At {}".format(s,i[1],i[0],i[2]))
    s=s+1