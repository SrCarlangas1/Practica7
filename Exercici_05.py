print "Dime una frase"
prime=raw_input()
pepe=list(prime)
print pepe
print "letra a sustituir"
susti=raw_input()
voc=["a","e","i","o","u"]
for vo in range(len(pepe)):
    pe=pepe.index(prime)
    pepe.insert(pe,susti)
print "La lista es ahora" , pepe

            
        
