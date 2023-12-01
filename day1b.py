nums=["zero","one","two","three","four","five","six","seven","eight","nine"]
tot=0
f=open("day1.txt","r")
for line in f:
    cali=[]#list for storing each
    c=0 # current position in line
    for letter in line:
        if letter.isdigit():#append letter if it is a digit
            cali.append(letter)
        else:
            posword=""            
            for k in range(c,len(line)):
                try:
                    posword=posword+line[k] #build a string from current character on
                except:
                    pass#deals with running out of characters
                if posword in nums:# if generated string is in list of numbers append index to cali (list of numbers found)
                    cali.append(str(nums.index(posword))) 
                    break #jumps out of loop when word found! - pants coding using a break!  
        c+=1#increment counter so not repeating first digit
    tot=tot+int(cali[0]+cali[-1])
print(tot)