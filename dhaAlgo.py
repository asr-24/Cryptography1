
def checkPrime(x):
    freq = 0
    for i in range (2,x):
        if (x%i == 0):
            freq+=1
        
    if (freq == 0):
        return True
    else:
        return False 
    

cont = 1

while (cont == 1):
    n = int(input("Enter n (prime) - "))
    g = int(input("Enter g (prime) - "))
    
    if (checkPrime(n) == True and checkPrime(g) == True):
        cont = 0
    else:
        print("Please ensure both the numbers are prime!")
        
        if (checkPrime(n) == False):
            print(f'{n} is a composite number!', end = "\n")
        else:
            print(f'{g} is a composite number!', end = "\n")
            
           

x = int(input("Enter x - "))
y = int(input("Enter y - "))

A = (g**x)%n
B = (g**y)%n

K1 = (B**x)%n
K2 = (A**y)%n

print(f'\n\nThe secret keys are as follows - \nK1 = {K1}\nK2 = {K2}')
        
