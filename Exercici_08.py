print "Dime una frase"
prime=raw_input()
pepe=list(prime)
print pepe
while ' ' in pepe:
    pepe.remove(' ')
print "La lista es ahora" , ''.join(pepe)
