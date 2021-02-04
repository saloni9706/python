import math
def guess_number(min,max,count,mid):
    count=count+1
    if mid>100:
        print("The number cannot exceed 100")
        return count
    answer=input("Is it "+str(mid)+" ? (yes/no) ")
    if answer == "no":
      greater=input("Is the number larger than "+str(mid)+" ? (yes/no) ")
      if greater=="yes":
         return guess_number(mid+1,max,count,math.ceil((mid+max)/2))
      else:
         max=mid-1
         return guess_number(min,max,count,math.floor((max+min)/2))
    else:
        return count
name=input("Hi, What is your Name ")
print("Hello "+name+"! Lets play a game!\nThink of a random number from 1 to 100,and I'll try to guess it!")
min=1
max=100
play_more="yes"
while play_more=="yes":
    if play_more == "yes":
        result=guess_number(min,max,0,(min+max)//2)
        print("Yeey! I got it in "+str(result)+" tries!")
        play_more=input("Do you want to play more? ")
    else:
        play_more="no"
print("Bye-bye​")
