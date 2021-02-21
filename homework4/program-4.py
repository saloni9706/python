# design URL shortener, similar to bit.ly 
def select_option():
    print("\n1. Get Short Url from original ")
    print("2. Get Original Url from short Url")
    print("3. Exit")
    choice=input("\nEnter your choice : ")
    return choice

# Hasing the original url and getting the last 5 chars for URL shortner 
def shorten_url(org_url):
    hash_value=str(hash(org_url))
    shorten_url="https://bit.ly/"+hash_value[-5:]
    all_urls[hash_value[-5:]]=org_url

    return shorten_url

# Get the last 5 chars from shortned URL and find the key in dictionary
def get_original_url(short_url):
    get_last_char=str(short_url[-5:])
    if get_last_char in all_urls.keys():
        return get_last_char
    else:
        return 0


all_urls={}
choice=select_option()
# Repeat untill user selects exit option
while choice!="3":
    if choice=="1":
        org_url=input("\nEnter Original URL : ")
        short_url=shorten_url(org_url)
        print("Short URL : ",short_url)

    elif choice=="2":
        short_url=input("\nEnter Short URL : ")
        url=get_original_url(short_url)
        if url==0:
            print("HTTP 404")
        else:
            print("Original URL : ",all_urls[url])

    else:
        exit()

    choice=select_option()

print("Thank You")

# Pro's and Con's
# This program is has limited scope i.e; If user enters same URL (original Url) twice, both will be hashed and and will be stored differently
# For MD5 It is impossible to generate two inputs that cannot produce the same hash function and It is impossible to generate a message having the same hash value.
# For UUID it is unique across applications but on the other side it uses more space