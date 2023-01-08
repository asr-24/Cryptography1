import numpy
import math
import collections
import tabulate as tb

substitutes = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
spaces= []


question = "XCIUIHTVOQVRLHJEYJXAVICEJFWXRVRUAAEPVPNEQLFZGFQEBXOIUXGIVJXVGLBRBXYIDBFZVKCSGHNITYJBXTSWXZHWZAYSEPINIIZWBRMITIFMQJRKLKASRIMIJPICEMIGGEIINWUTPZWVIFFEDRJXJXEHTISVNGOWRRVLIMZZGWLHZWZKFXHDRRASRXCEKKAOINYJIJLWJPVGGGXMSCSNXVVGTIKLXJXYIAKHVXREKTVZWLPLEERIEJGKGZQVRLBWNSDILBQZWLRSUPZXFVWVSQIIXZXGJRKIFMSAICIUMVJRZGUHQHYEMUTXDSEWXKSHXYILXGCRFPGZCKVFZAWIMIMIFBRMIJTGGWZXFEUHYMXFVVXVJVUYDREPXYSJBDZHNEJKEIXZWKNIYFPEXXHZVRPBNHBIWSJXBVQGPWFEICTSEFYIMTELBSIWJIJOMXIJRGPIIGICHMGZVKEAGGJQDYFBGVXZSFLFTHVJSNPOAZXZMLZOVCFXGZWJEJRXJHVGJRTOXYIUHQHYEMUTXDSEWKHPZPPMFMLZLRRVLSAXYIWGHPWVVLAMNEGTDBINFFXZPLZRKLWWEOEZWAGQJXZSFHZZVVPWVXMSEMUGIOAFVCLSMEKVWLXJRRRWEIXXISFBGYIMMUXMAXYIUHQHYEMUTXDSEWHKSQMUIJBWNIIZWWADXYEOTVMEEXKXIFMEKLASNITSEFYIMTELBSIWKLWIVJZZHWKGVRESLIVJZZHWMLZHRXSUIXELWWBXCEJHWLMBRVHLAIOITLFHPJKPWMVLOLRXAMGVRESLUIVGTIKLIYFPEFRXCMIHHTVOCNIVHRJXYENXEICJMDOIMFLPDXXNEEHLAIYMJGMLWDSEWOBXCMEXZXISITYLBZZFIEFVLVVVWLBPGSEKGBRBAYMDXXCIIIZTWISKCWMFZIEEVXGDWZSFPLZXYIJMSNIVODXKDWCELBSIAVQMLXRSIOOBXCGFRYKINWZRVNWOVPEUTHZQZGKIVDZRGQZVJYGWSGHJXYIJLXJGIEXMEIEGTJHEXLKLSMEYHIIKLINECPGYXCIDYDMMKPVGGFTZXZRYVSIGVVFLXCEKLSOIWIVRLAIASTYKHJNSDYUAHZFRXWUYOAVGSGEGPRKJXIOLRXOXADPCRWXHJRXSAGKCSEIKMEIHZRXHVHIUTMUPDGUITTXZESSMMLJASIKMXJTISLXGOPZFWKXTEEHKXGPVZXQBRWSKLGNVGENWSGHJYIXWVLISCSYR"

fromNotes = "UZ QSO VUOHXMOPV GPOZPEVSGZWSZ OPFPESX UDBMETSX AIZ VUEPHZHMDZSHZO WSFP APPD TSVPQUZW YMXUZUHSX EPYEPOPDZSZUFPOMB ZWP FUPZ HMDJ UD TMOHMQ"

new = "BIECYMBIECYMBIECYMBIECYMBIECYM"

def giveKeyList (key):
    keyList = []
    for i in key.upper():
        keyList.append(giveCorrespondingNumber(i))
   
    return keyList

def giveCorrespondingNumber (character):
    return (list(substitutes.keys())[list(substitutes.values()).index(character)])    
    


def encryptionWithKey (plainText, key):
    
    print(f'The original message is - {plainText}')
    
    for i in range (len(plainText)):
        if (plainText[i] == " "):
            spaces.append(i)
        
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

print(f'The encrypted message is - {decryptionWithKey(new, "HOKIES")}')



def displacementCoincidence (cipherText):
    displaced = []
    
    for i in range (1,15):
        new = []
        for j in range (i):
            new.append(" ")
        for k in cipherText:
            new.append(k)
        
        displaced.append(new)
        
    #print(displaced)
    
    disCoin = {}
    
    for i in range(14):
        
        j = 0                
        incidences = 0
                
        while (j<(len(cipherText))):

            if (cipherText[j] == displaced[i][j]):
                incidences+=1
            
            j+=1
            
        
        disCoin.update({i+1:incidences})
            
        
        
    disCoin = {k: v for k, v in sorted(disCoin.items(), key=lambda item: item[1], reverse = True)}
    return disCoin
            
            
        

print(f'By Displacement Coincidence - {displacementCoincidence(new)}')




def kasiskiTest (cipherText):
    
    
    diReps = []
    for i in range(len(cipherText) - 1):
        di = cipherText[i] + cipherText[i+1]
        
        
        for j in range (len(cipherText)):
            
            if (i == j or i+1 == j):
                continue
            elif (j+1 > len(cipherText)-1):
                break
            else:
                temp = cipherText[j] + cipherText[j+1]
                if (temp == di):
                    diReps.append([i+1,j+1])
                    
    distances = []
    for i in diReps:
        distances.append(abs(i[0] - i[1]))
        
    distances = list(set(distances))
    
    print(distances)
    
    return(math.gcd(distances[0],distances[1]))
    
#trial = "OPKVZQYEOPORBPKVZ"
print(f'By Kasiski Test - {kasiskiTest(new)}')     

def freidmanTest (cipherText):
    
    MgHeaders = [" "]
    FINALLY = []
    KEY = []
    
    for m in range (12,13):
        y = []
        qVec = []
        vVec = []
        MVec= []
        
        temp = []
        
        for i in range (26):
            temp.append(i)
        MVec.append(temp)
        
        for i in range(m):
            y.append([])
            qVec.append([])
            vVec.append([])
            MVec.append([])
            temp = "Mg" + str(i+1)
            MgHeaders.append(temp)
        
        
        
        for i in range(len(cipherText)):
            y[(i%m)].append(cipherText[i])
            
        
        print(f'\nFor m = {m}\n')
        
        for cipherText in y:
            
            cTtemp = cipherText
                        
            cipherText = "".join(cipherText)
            
            print(f'y{y.index(cTtemp)+1} = {cipherText}')
        
            allLetters = []
            for i in cipherText:
                if (i.isalpha()):
                    allLetters.append(i)
            
            allLetters = dict(collections.Counter(allLetters))
            
            letter_frequencies = {k: v for k, v in sorted(allLetters.items(), key=lambda item: item[1], reverse = True)}
            #return (letter_frequencies)
            
            n = len(cipherText)
            
            IcNum = 0
            
            for i in (list(letter_frequencies.keys())):
                fi = letter_frequencies[i]
                IcNum+=fi * (fi - 1)
                
            Ic = IcNum / (n * (n-1))
            
            print(f'Index of Coincidence = {Ic}\n')
            
            #print(len(cipherText))
            
            
            pVec = [0.082,0.015,0.028,0.043,0.127,0.022,0.020,0.061,0.070,0.002,0.008,0.040,0.024,0.067,0.075,0.019,0.001,0.060,0.063,0.091,0.028,0.010,0.023,0.001,0.020,0.001]            
                      
                  
            
            for i in range(65,91):
                qVec[y.index(cTtemp)].append(cipherText.count(chr(i))/len(cTtemp))
                
            
            
            for i in range (26):
                temp1 = []
                temp2 = []
                forP = 0
                for j in range (i, 26):
                    temp1.append(qVec[y.index(cTtemp)][j])
                    temp2.append(qVec[y.index(cTtemp)][j] * pVec[forP])
                    forP+=1
                    
                for j in range (0, i):
                    temp1.append(qVec[y.index(cTtemp)][j])
                    temp2.append(qVec[y.index(cTtemp)][j] * pVec[forP])                    
                    forP+=1
                
                vVec[y.index(cTtemp)].append(temp1)
                
                sumForM = 0
                for i in temp2:
                    k = i*100
                    sumForM+=k
                    
                MVec[y.index(cTtemp)+1].append(round(sumForM,2))            
            

            yay = MVec[y.index(cTtemp)+1].index(max(MVec[y.index(cTtemp)+1]))
            
            #print(yay)
            
            FINALLY.append(yay)
            
            #print(FINALLY)
            
            KEY.append(substitutes[yay])

        #print(MVec)
            
        MVec2 = []
        
        MVec2 = list(map(list, zip(*MVec)))
        
        #print(MVec2)
        
        #print(tb.tabulate(MVec2, headers = MgHeaders, tablefmt="grid"))
            
            
            
            
            
    print(f'Max values of Mg are {FINALLY}')
    print(f'The key is {KEY}\n\n')          
    #print(decryptionWithKey(question, "".join(KEY)))
            
                
                
        
                    
#print(len(question))
     
print("By Freidman Test - ")
freidmanTest(new)
        



    
    