vigKey = "latex"
permKey = {1:4,2:5,3:2,4:1,5:3}
permKeyInv = {1:4,2:3,3:5,4:1,5:2}

cipherText = "IEAEDURMZXALZTM"


substitutes = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

def giveKeyList (key):
    keyList = []
    for i in key.upper():
        keyList.append(giveCorrespondingNumber(i))
   
    return keyList

def giveCorrespondingNumber (character):
    return (list(substitutes.keys())[list(substitutes.values()).index(character)])    


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

def permutate (cipherText, key):
    new = []
    
    changed = []

    j = 0
    while (j<len(cipherText)):
        temp = []
        temp2 = []
        for i in range(len(key)):            
            if (j<len(cipherText)):        
                temp.append(cipherText[j])
                j+=1
                temp2.append('')
                
        new.append(temp)
        changed.append(temp2)
        
    print(new)
    
    for k in new:
        
        for i in range(len(k)):
            
            print(permKeyInv[i+1])
            changed[new.index(k)][i] = k[permKeyInv[i+1]-1]
            
    final = ""
    print(changed)
    for k in changed:
        final+=(''.join(k))
            
            
    return (final)



    
print(decryptionWithKey(permutate(cipherText, permKeyInv), vigKey))

#print(decryptionWithKey(cipherText, "EXALT"))
            

            
    