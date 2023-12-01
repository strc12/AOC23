tot=0
f=open("day1.txt","r")
for line in f:
    cali=[]
    for digit in line:
        if digit.isdigit():
            cali.append(digit)
    tot=tot+int(cali[0]+cali[-1])
f.close()
print(tot)