# Use decorator function you created for the previous homework and estimate how much operation on a dictionary is faster(or slower) than operation on a shelve
import time
import shelve
def f1_shelve_dic(func):
    def wrapper():
        print("Started")
        start=time.time()
        func()
        print("Ended")
        exe_time=time.time()-start
        return exe_time
    return wrapper

@f1_shelve_dic
def calculate_time_shelve():
    print("....Shelve....")
    sh=shelve.open("my_items")
    sh["list"]=[1,2,3,4]
    print(sh["list"])

@f1_shelve_dic
def calculate_time_dic():
    print("....Dictionary....")
    d={"list":{1,2,3,4}}
    print(d)

shelve_time=calculate_time_shelve()
dic_time=calculate_time_dic()
if shelve_time>dic_time:
    time_taken=shelve_time-dic_time
    print("Dictionary is faster than Shelve")
    print("Estimated Diff: {}".format(time_taken))
else:
    time_taken=dic_time-shelve_time
    print("Shelve is faster than Dictionary")
    print("Estimated Diff: {}".format(time_taken))
