import math as m

substitutes = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

def get_key(val):
    for key, value in substitutes.items():
         if val == value:
             return key

def checkPrime(x):
    freq = 0
    for i in range (2,x):
        if (x%i == 0):
            freq+=1
        
    if (freq == 0 and x != 1):
        return True
    else:
        return False 
    

cont = 1

while (cont == 1):
    p = int(input("Enter p (prime) - "))
    q = int(input("Enter q (prime) - "))
    
    if (checkPrime(p) == True and checkPrime(q) == True):
        cont = 0
    else:
        print("Please ensure both the numbers are prime!")
        
        if (checkPrime(p) == False and checkPrime(q) == False):
            print("Both are composite numbers!", end = "\n")
        elif (checkPrime(p) == False):
            print(f'{p} is a composite number!', end = "\n")
        else:
            print(f'{q} is a composite number!', end = "\n")
           
plainList = []
cipherList = []
plainListNew = []
finalText = []


n = p * q
phiN = (p-1)*(q-1)

e = 0
for i in range (15, phiN):
    if m.gcd(i,phiN) == 1:
        e = i
        break

d = 0    
for i in range(2,1000):
    if (e*i)%phiN == 1:
        d = i
        break


        
plainText = input("Enter the plaintext that Bob wishes to send - ")        


for i in plainText:
    plainList.append(get_key(i))
    

#encryption using e

for i in plainList:
    cipherList.append((i**e)%n)
    

print(f'Bob sends {cipherList}')
print(f'Alice receives {cipherList}')


#decryption using private key d

for i in cipherList:
    plainListNew.append((i**d)%n)
    
    
for i in plainListNew:
    finalText.append(substitutes[i])
    
finalText = ''.join(finalText)

print(f'Alice translates the message to read {finalText}')
    

