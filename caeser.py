substitutes = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

def get_key(val):
    for key, value in substitutes.items():
         if val == value:
             return key

print("Caesar Cipher")
ch = int(input("Encrypt (1)/Decrypt (2) - "))
en = []
if (ch == 1):
    og = input("Enter the text to be encrypted - ")
    key = int(input("Enter key - "))
    
    for i in og:
        #print(i)
        if (i.isalpha()):
            t = (int(get_key(i.upper())) + key)%(26)
            en.append(substitutes[t])
        else:
            en.append(i)

    print("The encrypted text is - ",''.join(en))
else:
    og = input("Enter the text to be decrypted - ")
    ch2 = int(input("Enter 1 to brute force, 2 if the key is known - "))
    if (ch2 == 2):
        key = int(input("Enter key - "))
        for i in og:
            #print(i)
              if (i.isalpha()):
                 t = (int(get_key(i.upper())) - key)%(26)
                 en.append(substitutes[t])
              else:
                 en.append(i)
        print("The decrypted text is - ",''.join(en))
    else:
        key = 0
        for key in range(1,26):
            en = []
            for i in og:
            
                if (i.isalpha()):
                    t = (int(get_key(i.upper())) - key)%(26)
                    en.append(substitutes[t])
                else:
                    en.append(i)
                
            print("W/ key - ", key, end = " ~ ")
            print("The decrypted text is - ",''.join(en))
            
            
