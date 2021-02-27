# Encryption and decryption
key=4
def func_encryt(cipher):
    def inner(string_encpt,key):
        print("Started Encryption")
        val=cipher(string_encpt,key)
        print("Ended Encryption\n")
        return val
    return inner


def func_decrypt(decryption):
    def inner_decrypt(string_encpt,key):
        print("Started Decryption")
        val=decryption(string_encpt,key)
        print("Ended Decryption")
        return val
    return inner_decrypt

# Encryption
@func_encryt
def cipher(string_encpt,key):
    encrypted_string=""
    for i in range(len(string_encpt)):
        get_char=string_encpt[i]
        encrypted_string+=chr((ord(get_char)+key-97)%26 +97)
    print(encrypted_string)
    return encrypted_string

# Decryption
@func_decrypt
def decryption(enc_string,key):
    alpha = "abcdefghijklmnopqrstuvwxyz "
    
    result= ""
    for i in enc_string:
        if i in alpha:
            num = alpha.find(i)
            num = num - key
            if num < 0:
                num = num + len(alpha)
            result = result + alpha[num]
        else:
            result = result + i

    print(result)

# Assumption made:
# No UpperCase and No Digits/Symbols
encrypted_string=cipher("decorator",key)
decryption(encrypted_string,key)