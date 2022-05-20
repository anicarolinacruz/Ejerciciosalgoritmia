valorDescuento = 0
valorCompra=int(input("Digite el valor de la compra: "))
print ("El valor de la compra ingresada es: ", valorCompra)

if valorCompra>= 50.000:
    print ("participa en descuento")
    colorBalota = str(input("Ingrese el color de la balota: "))
    mayusculaBalota = colorBalota.upper()
    match mayusculaBalota:
        case 'ROJO':
            valorDescuento=100

        case 'VERDE':
            valorDescuento=50

        case 'BLANCO':
            valorDescuento=30

        case 'NEGRO':
            valorDescuento=20

        case 'AMARILLO':
            valorDescuento=10
    
    total = float(valorCompra - ((valorCompra * valorDescuento) / 100))    

else: 
    valorDescuento = 0
    total = valorCompra
    print ("No aplica al descuento")




print ("Valor del descuento = ", valorDescuento, "%")
print("El valor total a pagar es = ", total)