# write a program that will take a command line argument of full path and prints True if the file/directory at the provided location is present 
# Change program such that it runs indefinitely, monitoring a file/directory at a certain location 
import sys,os

arguments=sys.argv
arguments.pop(0)
for location in arguments:
    if not os.path.exists(location):
        print(os.path.exists(location))
    else:
        while os.path.exists(location)==True:
            is_active=1
        
        print("Alert")

# sample command :->>> python program1.py C:\Users\python\homework6\test_prog1.txt
# 