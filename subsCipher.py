import collections 
import tabulate

with open('cipherText.txt','r') as f:
    cipherText = f.read()
    cipherText = cipherText.upper()
    with open('cipherText.txt','w') as f2:
        f2.write(cipherText)
    
cT = cipherText.split(' ')

def letterFrequencies ():
    allLetters = []
    for i in cipherText:
        if (i.isalpha()):
            allLetters.append(i)
    
    allLetters = dict(collections.Counter(allLetters))
    
    letter_frequencies = {k: v for k, v in sorted(allLetters.items(), key=lambda item: item[1], reverse = True)}
    return (letter_frequencies)
    


def digramsAndTrigrams ():
    digrams = []
    trigrams = []
    for i in cT:
        if (len(i) == 2):
            digrams.append(i)
        elif (len(i) == 3):
            trigrams.append(i)
        
    fD = dict(collections.Counter(digrams))
    fT = dict(collections.Counter(trigrams))
        
    fD_final = {k: v for k, v in sorted(fD.items(), key=lambda item: item[1], reverse = True)}
    fT_final = {k: v for k, v in sorted(fT.items(), key=lambda item: item[1], reverse = True)}
    
    return (fD_final, fT_final)

def digramSuggestions ():
    
    print("The most common digrams are (in decreasing order): \nTH, HE, IN, ER, AN, RE, ED, ON, ES, ST,\nEN, AT, TO, NT, HA, ND, OU, EA, NG, AS,\nOR, TI, IS, ET, IT, AR, TE, SE, HI, OF")
        
    print("Frequent digrams that make sense as a word - ")
    print("HE, IN, AN, ON, AT, TO, AS, OR, IS, IT, HI, OF")
    
    print("Frequent Digrams that aren't standalone words - ")
    print("TH, ER, RE, ED, ES, ST, EN, NT, HA, OU, EA, NG, TI, ET, AR, TE")
    
def trigramSuggestions ():
    print("The twelve most common trigrams are:\nTHE, ING, AND, HER, ERE, ENT,\nTHA, NTH, WAS, ETH, FOR, DTH.")
    
    print("Frequent trigrams that make sense as a word - ")
    print("THE, HER, WAS, FOR")
    
    print("Frequent trigrams that aren't standalone words - ")
    print("ING, ERE, ENT, THA, NTH, ETH, DTH")
    


def tabulateData (headers, data):
    print(tabulate.tabulate(data, headers = headers, tablefmt="github"))
    
    
doneLetters = {}

def startReplacing ():
    
    fread = open('cipherText.txt','r')
    fwrite = open('plainText.txt', 'w')

    cipherText = fread.read()
    
    
    
    for i in range (26):
        
        new = ''
        
        
        
        for j in range (len(cipherText)):
            if (cipherText[j] in list(doneLetters.keys())):
                print(cipherText[j])
                cipherText = cipherText.replace(cipherText[j],doneLetters[cipherText[j]])
                
            else:
                continue
                
        print(cipherText)
        
        change = input("What you want to replace, the letter you want to replace it with (0 to stop, 9 for dict) - ")
        if (change == '0'):
            break
        elif (change == '9'):
            print(doneLetters)
            
        else:
            if (' ' in change):
                change = change.split(', ')
            else:
                change = change.split(',')
            replaceThis = change[0].upper()
            withThis = change[1].lower()
            
            if (replaceThis in doneLetters):
                print(f"Letter already replaced with {doneLetters[replaceThis]} ")
            else:
                try:
                    fwrite.write(cipherText.replace(replaceThis, withThis))
                    doneLetters.update({replaceThis: withThis})
                except:
                    fread.close()
                    fwrite.close()


    fread.close()
    fwrite.close()
    
        
    
    
print(letterFrequencies())
print(digramsAndTrigrams())
startReplacing()