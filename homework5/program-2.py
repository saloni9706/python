#  Recursively return the number of "ears" in the bunny line 1, 2, ... n 
def bunnyEars(bunnies):
    if bunnies==0:
        return 0
    else:    
        if(bunnies%2==0):
            return bunnyEars(bunnies-1)+3
        else:
            return bunnyEars(bunnies-1)+2
result1=bunnyEars(2)
print(result1)