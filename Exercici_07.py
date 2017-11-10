lila=[]
print "Dime una frase"
prime=raw_input()
lila.append(prime)
voc=["a","e","i","o","u"]
secu=0
for k in range(0, len(prime)):
    if prime[k] in voc:
        secu = secu+1
print "el numero de vocales son" , secu
            
        
