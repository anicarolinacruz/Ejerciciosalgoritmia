#funcion.
def listaVacia(lista):
    print('\n\t---Lista---\n')
#ciclo para guardar los valores en la lista.
    while True:
        valores=int(input('digite los valores :  '))
#longitud limitada de la lista y los valores que siga ingresando ya no sera posible.
        if len(lista)<10:
            valores not in lista
            lista.append(valores)
#arrojara un mensaje cuando la lista ya esta limitada.
        else:
            print(f'\nla longitud maxima es--> {len(lista)}\nsalir del programa--> (S/s) o (N/n)')
#salir o seguir en el programa. Si persiste, se seguira arrojando el mensaje (longitud maxima-->10).
            salir=input('salir: ')
            if salir=='S' or salir=='s':
                print('-----------------------------------------------------------------------------')
                print(f'Valores Numericos--> {lista}\nLogitud de la lista : {len(lista)}')
                break
            elif salir=='N' or salir=='n':
                continue 
#programa principal
lista=list()
listaVacia(lista)