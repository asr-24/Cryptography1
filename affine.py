import collections 

substitutes = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

def get_key(val):
    for key, value in substitutes.items():
         if val == value:
             return key


def giveInverse (a,b):
    u = [[1],[0],[a]]
    v = [[0],[1],[b]]
    q = [0]
    
        
    def newQValue(x,y):
        return (x//y)
    
    def newU(x,n):
        if (n == 1):
            return (v[0][x-1])
        elif (n == 2):
            return (v[1][x-1])
        else:
            return (v[2][x-1])
    
    def newV(x,n):
        if (n == 1):
            return (u[0][x-1] - q[x]*v[0][x-1])
        elif (n == 2):
            return (u[1][x-1] - q[x]*v[1][x-1])
        else:
            return (u[2][x-1] - q[x]*v[2][x-1])
        
    n = 0
    
      
    
    while True:
        n+=1
        q.append(newQValue(u[2][n-1], v[2][n-1]))
        
        for i in range(3):
            u[i].append(newU(n,i+1))
        for i in range(3):
            v[i].append(newV(n,i+1))
        
        
        if (v[2][n] == 0):
            break
                 
    
    if (u[2][n] == 1):
        return((u[0][n])%b)   



ch = int(input("Encrypt (1)/Decrypt (2) - "))
en = []
if (ch == 1):
    og = input("Enter the text to be encrypted - ")
    key = input("Enter the key values - ").split(', ')
    
    for i in og:
        #print(i)
        if (i.isalpha()):
            t = (int(get_key(i.upper()))*int(key[0]) + int(key[1]))%(26)
            en.append(substitutes[t])
        else:
            en.append(i)

    print("The encrypted text is - ",''.join(en))
else:
    og = input("Enter the text to be decrypted - ")
    ch2 = int(input("Enter 1 to brute force, 2 if the key is known - "))
    if (ch2 == 2):
        key = input("Enter key - ").split(', ')
        for i in og:
            #print(i)
              if (i.isalpha()):
                 t = (giveInverse(int(key[0]),26) * (int(get_key(i.upper())) - int(key[1])))%(26)
                 en.append(substitutes[t])
              else:
                 en.append(i)
        print("The decrypted text is - ",''.join(en))
    else:
        def letterFrequencies ():
            allLetters = []
            for i in og:
                if (i.isalpha()):
                    allLetters.append(i)
            
            allLetters = dict(collections.Counter(allLetters))
            
            letter_frequencies = {k: v for k, v in sorted(allLetters.items(), key=lambda item: item[1], reverse = True)}
            return (letter_frequencies)        
        
        print(letterFrequencies())
        
        print("Enter what letter from the dict you think maps to which letter")
        
        guess1 = (input("Guess 1 - Cipher, Plain - ").upper()).split(', ')
        guess2 = (input("Guess 2 - Cipher, Plain - ").upper()).split(', ')
        
        print("Your equations - ")
        a1 = get_key(guess1[1])
        a2 = get_key(guess2[1])
        c1 = get_key(guess1[0])
        c2 = get_key(guess2[0])
        
        print(f'{a1}a + b = {c1}')
        print(f'{a2}a + b = {c2}')
        
        print(f'{a2*-1 + a1}a = {c2*-1 + c1}')
        temp = 0
        
        if (a2*-1 + a1 < 0):
            print(f'{-1*(a2*-1 + a1)}a = {-1*(c2*-1 + c1)} mod 26')
            #temp = -1*(c2*-1 + 10) * giveInverse(-1*(a2*-1 + a1), 26)
        else:
            print(f'{1*(a2*-1 + a1)}a = {1*(c2*-1 + c1)} mod 26')
            #temp = 1*(c2*-1 + 10) * giveInverse(1*(a2*-1 + a1), 26)
            
        
        
        print(f'a = {temp} mod 26')
        
        a = temp%26
        a = 9
        print(f'a = {a} mod 26')
        
        print(f'{a1*a} + b mod 26 = {c1}')
        print(f'{a1*a} + b = {c1} mod 26')
        print(f'b = {c1 - a1*a} mod 26')
        
        b = (c1 - a1*a)%26
        print(f'b = {b} mod 26')
        
        
        key = [a, b]
        for i in og:
            #print(i)
              if (i.isalpha()):
                 t = (giveInverse(key[0],26) * (int(get_key(i.upper())) - key[1]))%(26)
                 en.append(substitutes[t])
              else:
                 en.append(i)
        print("The decrypted text is - ",''.join(en))
        
        
        
        
        
        
        
        
        
        
            
            



