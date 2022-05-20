#funcion.
def fibonacci(lista_fib):
    fn1=0
    fn2=1
    print('\n\t<--Ingrese un número para comenzar la secuencia Fibonacci-->\n')
#el usuario podra digitar un numero para que se realice la secuencia de fibonacci.
    while True:
        numero_fibonacci=int(input('Digite un numero : '))
#si el usuario digita un numero mayor a 1 se detendra y pasara al siguiente bucle (for).
        if numero_fibonacci>1:
            break
#de lo contario si digita un numero menor a 1 seguira en el bucle while hasta que sea mayor o igual a 1.
        else:
            print('el numero debe ser mayor o igual a 1')
    print('\n\t<--Secuencia Fibonacci-->\n')
    lista_fib.append(1)
#en el bucle for se realizara la operacion de fibonacci (fn=fn-1+fn-2).
    for i in range(numero_fibonacci-2):
        fn3=fn1+fn2
        fn1=fn2
        fn2=fn3
#se agregaran los valores de fibonacci a una lista vacia.
        lista_fib.append(fn3)
    print(lista_fibonacci)
#programa principal.
lista_fibonacci=list()
fibonacci(lista_fibonacci)