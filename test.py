def signe(x):
    if (x>0):
        print(x, "positif")
    elif x  == 0:
        print(x, "nul")
    else:
        print(x, "negatif") 
        
        
signe(5)

for i in range (10, -10, -1):
    signe(i)
    
x = 0
while x<10:
    print (x)
    x += 1

