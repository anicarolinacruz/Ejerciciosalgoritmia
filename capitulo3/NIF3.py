digitoControl= ('TRWAGMYFPDXBNJZSQVHLCKE');
nif=input("digite su NIF: ");
x= digitoControl[int(nif) % 23];

print ("digito control = " + nif + x);