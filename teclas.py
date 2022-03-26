tecla1=input("digite primera tecla: ")
tecla2=input("digite segunda tecla: ")
tecla3=input("digite tercera tecla: ")
tecla4=input("digite cuarta tecla: ")

if tecla1=='ctrl' and tecla2=='alt' and tecla3=='t':
    print("terminal de Ubuntu")

elif tecla1=='super' and tecla2=='L' or 'ctrl' and tecla3=='alt' and tecla4=='L':
    print("bloquea pantalla")

elif tecla1=='super' and tecla2=='D' or 'ctrl' and tecla3=='Alt' and tecla4=='D':
    print("mostrar escritorio")

else:
    print("accion incorrecta")
