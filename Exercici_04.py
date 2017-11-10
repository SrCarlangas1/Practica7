print "Dime una frase"
prime=raw_input()
pepe=list(prime)
print pepe
while ' ' in pepe:
    manu=pepe.index(' ')
    pepe.remove(' ')
    pepe.insert(manu,"*")
print "La lista es ahora" , pepe
