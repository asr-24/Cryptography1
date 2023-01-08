import math

coprimes = []

for i in range (1,100):
    if (math.gcd(100,i) == 1):
        coprimes.append(i)
    else:
        continue
    
print(len(coprimes))
print(coprimes)
        