myMessge = input("Enter your message - ")
keyword = input("Enter your keyword - ")

key = list(keyword) 
if len(myMessge) == len(keyword): 
   key = keyword
else: 
   for i in range(len(myMessge)-len(keyword)): 
       k = key[i % len(keyword)]
       key.append(k) 
key = "".join(key)
  
def encryptionFxn(myMessge, key): 
  cipherText = [] 
  for i in range(len(myMessge)): 
    x = (ord(myMessge[i]) + ord(key[i]))%26
    x = x + ord('A') 
    charX = chr(x)
    cipherText.append(charX) 
    cipherTextFinal = "".join(cipherText)
  return(cipherTextFinal) 

def decryptionFxn(cipherText, key): 
  plainText = [] 
  for i in range(len(cipherText)): 
    x = ((ord(cipherText[i]) -ord(key[i]) + 26) % 26) + ord('A')
    charX = chr(x)
    plainText.append(charX) 
    plainTextFinal = "".join(plainText)
  return(plainTextFinal) 

cipherText = encryptionFxn(myMessge, key) 
print("Encrypted message:", cipherText) 
print("Decrypted message:", decryptionFxn(cipherText, key)) 