#funcion.
def motos(elementos,cadena,ordenar):
    print('\n\t---Contenido de la lista---\n')
#los elementos de la lista se visualizaran fuera de ella con su respectiva enumeracion.
    contador=1
    for i in elementos:
        print(f'{contador}. {i}')
        contador+=1
    print(f'\n\t---Cadena de caracter---\n\n{cadena}\n\n\t---Ordenar lista---\n\n{ordenar}')
#los elementos de la lista se visualizaran fuera de ella organizada alfabeticamente y enumerada.
    contador=1
    for x in ordenar:
        print(f'{contador}. {x}')
        contador+=1
#programa principal.
elementos=['yamaha','suzuki','honda','ktm','ayco','boxer','kawasaki','kymko','akt','auteco']
#se observara la lista en cadena de caracter y organizada alfabeticamente.
cadena=", ".join(elementos)
ordenar=sorted(elementos)
motos(elementos,cadena,ordenar)
#funcion.
def marcas(longitud):
#el usuario podra buscar el elemento que se encuentra en la lista.
    while True:
        buscar=str(input('\ndigite el elemento que desea buscar (x paras salir) : '))
        if buscar=='x':
            print(':)')
            break
        if buscar in elementos:
            print(f'\n\t---Resultado---\n\n{buscar}')
#si el usuario digita una marca no existente se arrojara un mensaje de abvertencia.
        else:
            print('marca no existente')
    print('\n\t---Longitud de la lista---\n')
    print(longitud)
#programa principal.
longitud=len(elementos)
marcas(longitud)