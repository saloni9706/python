string=input("Enter string : ")
lst=[]
print("Enter array of length "+str(len(string))+"")
for i in range(0,len(string)):
    ele=int(input("indices["+str(i)+"] : "))
    lst.append(ele)
new_string=list(string)

for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i] > lst[j]):    
            temp = lst[i]    
            lst[i] = lst[j]    
            lst[j] = temp

            temp2=new_string[i]
            new_string[i]=new_string[j]
            new_string[j]=temp2

print("Output: "+str("".join(new_string)))