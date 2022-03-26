from email import charset
import string

contador=0
texto=input('ingrese palabra: ')
alfabeto= ('AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz')

for i in texto:
    if i in alfabeto:
        contador+=1
        
    else:
        print('Todos los carcteres no son alfabeticos')
if contador==len(texto):
    print('todos los caracteres son alfabeticos')