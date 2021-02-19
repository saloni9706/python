#  leetcode 2 sum
array_size=int(input("Enter size of array : "))
nums=[]
output=[]
for i in range(0,array_size):
    ele=int(input("indices["+str(i)+"] : "))
    nums.append(ele)
target=int(input("Enter target : "))
flag=0
for i in range(len(nums)):
    if flag==0:
        for j in range(i+1,len(nums)):
            sum_num=nums[i]+nums[j]
            if(sum_num==target):
                output.append(i)
                output.append(j)
                flag=1
                break

print(output)   
