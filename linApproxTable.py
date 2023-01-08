import numpy as np
import tabulate as tb

#inputs = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
#outputs = ['1110','0100','1101','0001','0010','1111','1011','1000','0011','1010','0110','1100','0101','1001','0000','0111']


inputs = ['000','001','010','011','100','101','110','111']
outputs = ['110','101','001','000','011','010','111','100']

n = len(inputs)

linApp = np.zeros((n,n))


hhh = 0
for ip in range (n):
    for op in range (n):
        yeses = 0 
        nos = 0
        
        bits = len(inputs[0])
        
        bitString = '0' + str(bits) + 'b'
        
        binReprInput = format(ip, bitString)
        binReprOutput = format(op, bitString)
        
        #print(binReprInput)
        
        ipSelect = []
        opSelect = []
        
        for m in range(len(binReprInput)):
            if (binReprInput[m] == '1'):
                ipSelect.append(m)
            if (binReprOutput[m] == '1'):
                opSelect.append(m)
        
        for k in range (n):
            ipXor = 0
            opXor = 0
            
            for q in range(len(inputs[k])):
                if (q in ipSelect):
                    ipXor^=int(inputs[k][q])
                if (q in opSelect):
                    opXor^=int(outputs[k][q])
            
            if (ipXor == opXor):
                yeses+=1
            else:
                nos+=1
                
        linApp[ip][op] = yeses
        #print(hhh)
        hhh+=1
        
    
normalizedLinApp = linApp - (len(linApp)/2)
print(tb.tabulate(normalizedLinApp, inputs, tablefmt="github"))


