# Write a function count_frequency that takes a list of words as an argument, counts how many times each word appears in the list, and then returns this frequency listing as a Python dictionary
def count_frequency(mylist):
    cnt_freq={}
    for item in mylist:
        if(item in cnt_freq):
            cnt_freq[item] += 1
        else:
            cnt_freq[item]=1
    return cnt_freq

mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
output=count_frequency(mylist)

print(output)
