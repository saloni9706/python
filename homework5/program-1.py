# Use generator functions to create your own version of range function, call it my_range. Do not use the python's range function in the code.
def my_range(start,end,counter):

    while start<end:
        yield start
        start=start+counter
counter=1
print("Example 1 : ")
for i in my_range(0,5,counter):
	print(i)
counter=2
print("Example 2 : ")
for i in my_range(0,5,counter):
	print(i)    