import tabulate as tb

print("Division Algorithm Implementation")
print("Arushi Rai - K047")

a = int(input("Enter the first number  - "))
b = int(input("Enter the second number - "))

headers = ["u1 ","v1 ","u2 ","v2 ","u3 ","v3 ","q "]
u = [[1],[0],[a]]
v = [[0],[1],[b]]
q = [0]

tableData = []
tableData.append([u[0][0],v[0][0],u[1][0],v[1][0],u[2][0],v[2][0],q[0]])

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

print(tb.tabulate(tableData, headers = headers, tablefmt="grid"))   

while True:
    n+=1
    q.append(newQValue(u[2][n-1], v[2][n-1]))
    
    for i in range(3):
        u[i].append(newU(n,i+1))
    for i in range(3):
        v[i].append(newV(n,i+1))
        
      
    tableData.append([u[0][n],v[0][n],u[1][n],v[1][n],u[2][n],v[2][n],q[n]])
    
    print(f'\n\nIteration number {n}')
    print(tb.tabulate(tableData, headers = headers, tablefmt="grid"))   
    
    if (v[2][n] == 0):
        break
         
    
print("\n\n\nFinal table (at v3 = 0) - ")    
print(tb.tabulate(tableData, headers = headers, tablefmt="grid"))   

print(f'\n\ngcd({a},{b}) = {u[2][n]}')
print(f'({a})({u[0][n]}) + ({b})({u[1][n]}) = {u[2][n]}')
    


def rules():
    
    print("The new q is the greatest integer less than or equal to the quotient of the old u3 and v3.")
    print("The new ui is the old vi")
    print("The new vi = old ui − ( current q)( old vi)")
    print("We do this multiple times, until we produce a row where v3 = 0")
    print("GCD is u3")
    print("a is u1 and b is u2")