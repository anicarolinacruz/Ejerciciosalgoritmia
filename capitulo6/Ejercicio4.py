#funcion
def narrativa(key,values,key_2,values_2,key_3,values_3):
#se imprime un menú de las diferentes opciones de genero literario.
    print('\n\t<--Bienvenido a Tú libro-->\n')
    print('Elige una de las siguiente opciones:\n')
    print('[1]Género Narrativo\n[2]Género Dramático\n[3]Género Líterario\n[S/s]Salir del programa ->\n')
#se realiza un bucle while para preguntarle al usuario que opcion desea escojer.
    while True:
        opcion_generos=input('Digite la opcion para vizualizar las catergorias : ')
#si el usuario digita 1, se extraera la informacion de genero narrativo.
        if opcion_generos=='1':
#se crea un bucle for para extraer la llave del diccionario y mostrar por pantalla.
            for i in key:
                print(f'\n{i}')
#se crea un segundo bucle for, creando una variables n1,n2,n3 donde se almacenara los difenretes libros.
            for j in values:
                n1,n2,n3=j
#se imprimira los nombres de los libros en las llaves fuera del diccionario con la funcion .format()
            print('\n{}\n{}\n{}'.format(n1,n2,n3))
#si el usuario digita 2, se extraera la informacion de genero dramático.
        if opcion_generos=='2':
            for i in key_2:
                print(f'\n{i}')
            for j in values_2:
                d1,d2,d3=j
            print('\n{}\n{}\n{}'.format(d1,d2,d3))
#si el usuario digita 3, se extraera la informacion de genero lírico.
        if opcion_generos=='3':
            for i in key_3:
                print(f'\n{i}')
            for j in values_3:
                l1,l2,l3=j
            print('\n{}\n{}\n{}'.format(l1,l2,l3))
#se realiza una opcion si el usuario desea salir del programa
        if opcion_generos=='s' or opcion_generos=='S':
            print('¡Gracias! por visitarnos')
            break
#si el numero es mayor a la opcion indicada (3), arrojara un mensaje de abvertencia.
        if opcion_generos>'3':
            print('Opcion invalida, opciones validas [1/2/3]')
#diccionario de los diferentes generos (narrativo,drámatico,lírico)
narrativo={'Narrativa':['La vorágine','Don Quijote de la mancha','Con la soga al cuello'],}
dramatico={'Dramático':['El hechizo del agua','Primero es ella','Hasta que salga el sol']}
literario={'Líterario':['Los Heraldos negros','Los versos del capitán','Cantar del Mio Cid']}
#llaves y valores de los diccionarios.
llave=list(narrativo.keys());llave_2=list(dramatico.keys());llave_3=list(literario.keys())
valores=list(narrativo.values());valores_2=list(dramatico.values());valores_3=list(literario.values())
#programa principal
narrativa(llave,valores,llave_2,valores_2,llave_3,valores_3)
