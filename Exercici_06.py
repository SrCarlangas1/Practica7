print "Dime un nombre"
prime=raw_input()
pepe=list(prime)
print pepe
print "Dime un caracter"
susti=raw_input()
if susti in pepe:
    print "El caracter esta en tu nombre"
else:
    print "El caracter no esta en tu nombre"
