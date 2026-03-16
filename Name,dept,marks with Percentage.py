name=['Anu','Ram','Raj','Bala','Abi','Ravi']
marks=[80,60,38,75,35,90]
dept=['CSE','IT','CSE','AI&DS','ECE','ECE']
s=1
for i in range(6):
    if(marks[i])>40:
        print("{}.{}from {} dept,has scored {}%".format(s,name[i],dept[i],marks[i]))
        s=s+1