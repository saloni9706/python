# Create a decotor function that will take any function, with any number of arguments and print the time it takes to execute it.
import time

def f1(func):
    def wrapper(*arg,**named_arguments):
        print("Started")
        start=time.time()
        val=func(*arg,**named_arguments)
        print("Ended")
        print("Time to execute : {}".format(time.time()-start))
        return val
    return wrapper
@f1
def calculate_time(*arg,**named_arguments):
    print("Args: ",*arg,**named_arguments)

calculate_time(4,2,5,5,2)