plainText = "hereishowitworks"
key = "cipher"
substitutes = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

plainText = plainText.upper()
key = key.upper()
keyList = []
for i in key:
    keyList.append(list(substitutes.keys())[list(substitutes.values()).index(i)])

plainTextList = []
for i in plainText:
    plainTextList.append(list(substitutes.keys())[list(substitutes.values()).index(i)])
    
    
i = 0
encodedText = []
breakCheck = 0

print(len(plainTextList))

while (i<len(plainTextList)):
    if (breakCheck == 1):
        break
    else:
        print("i am i",i)
        
        char = plainTextList[i]
        
        j = 0
        
        while (j<len(keyList) and i<len(plainTextList)):
            encodeIndex = (char+(keyList[j]))%26
            encodedText.append(substitutes[encodeIndex])
            i+=1
            j+=1
            char = plainTextList[i]
        else:
            print(f'{i} and {j} and here')
            if (i>=len(plainTextList)):
                breakCheck = 1
                break
        
              


print(encodedText)