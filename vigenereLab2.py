substitutes = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

def giveKeyList (key):
    keyList = []
    for i in key.upper():
        keyList.append(giveCorrespondingNumber(i))
   
    return keyList

def giveCorrespondingNumber (character):
    return (list(substitutes.keys())[list(substitutes.values()).index(character)])    
    

def encryptionWithKey (plainText, key):
    
    print(f'The original message is - {plainText}')
    
    keyList = giveKeyList(key)
    
    plainTextList = []
    for i in (plainText.replace(" ", "")).upper():
        plainTextList.append(giveCorrespondingNumber(i))
        
    i = 0
    encodedText = []
    
    while (i<len(plainTextList)):
        char = plainTextList[i]
        
        j = 0
        
        while (j<len(keyList) and i<len(plainTextList)):
            encodeIndex = (char+(keyList[j]))%26
            
            encodedText.append(substitutes[encodeIndex])
            #print(f'{encodedText}\n{char}\n{j}')
            i+=1
            j+=1
            if (i<len(plainTextList)):
                char = plainTextList[i]
            
         
    return ("".join(encodedText))



def decryptionWithKey (cipherText, key):
    
    keyList = giveKeyList(key)
    

    cipherTextList = []
    for i in cipherText:
        cipherTextList.append(giveCorrespondingNumber(i))

    i = 0
    decodedText = []

    while (i<len(cipherTextList)):
        char = cipherTextList[i]

        j = 0

        while (j<len(keyList) and i<len(cipherTextList)):
            decodeIndex = (char-(keyList[j]))%26

            decodedText.append(substitutes[decodeIndex])
            i+=1
            j+=1
            if (i<len(cipherTextList)):
                char = cipherTextList[i]
    
                
    return "".join(decodedText)



cipher = encryptionWithKey("TAKEHOMEQUIZ", "EXALT")

print(f'The ciphertext is - {cipher}')

print(f'The decrypted text is - {decryptionWithKey("CISHAWGIUHOGIJZMU","ARUSHI")}')




