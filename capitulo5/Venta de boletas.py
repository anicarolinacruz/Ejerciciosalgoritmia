print('\n\tventa de boletas')
cantidad_restante=10
cantidad_total=0
lista_ID=list()
confirmacionCompra = True
while confirmacionCompra == True:
    compro = False
#presentar cedula de ciudadania
    ingrese_ID=int(input('digite el numero de cedula : '))
#si el documento existe rechazar la venta de la boleta
    if ingrese_ID not in lista_ID:
        print('bienvenido a la compra de su boleta')
#cantidad de boletas que desea comprar
        venta_boleta=int(input('digite la cantidad de boletas : '))
        if venta_boleta<=4 and cantidad_restante>=venta_boleta:
            cantidad_restante-=venta_boleta
            cantidad_total+=venta_boleta
            print('su compra ha sido exitosa')
#agregar cedula de ciudadania a un vector
            lista_ID.append(ingrese_ID)
            compro = True
            print('\n\tventa de boletas')
#cuando la cantidad llegue a cero muestre un mesaje y finalice
            if cantidad_restante==0:
                print('boletas agotadas')
                break
            compro = False
        if venta_boleta>=5 or (cantidad_restante<venta_boleta and cantidad_restante != 0 and compro == False):
                print('cantidad invalida de boletas maximo (3)')
                print('La cantidad de boletas disponibes es: ', cantidad_restante)
        seguirCompra=input('Se va a registrar una nueva compra?  S/N : ')
        if seguirCompra == 'n' or seguirCompra == 'N':
            confirmacionCompra = False
    else:
        print('el documento ya existe')
        compro = False
print(f'\nlista_ID : {lista_ID}\ncantidad de boletas disponibles : {cantidad_restante}\ncantidad de boletas compradas : {cantidad_total}')



'Se cambio lista_ID.append(ingrese_ID) de la linea 9 a la linea 15 para que se haga el registro en la lista solo si compra'