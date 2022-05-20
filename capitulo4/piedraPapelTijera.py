persona1=input("opcion de persona 1: ")
persona2=input("opcion de persona 2: ")

if persona1==persona2:
    print ("empate")
elif persona1=="papel" and persona2=="piedra":
    print ("persona 1 gana! el papel envuelve a la piedra")
elif persona1=="papel" and persona2=="tijera":
    print ("persona 2 gana! la tijera corta el papel")
elif persona1=="piedra" and persona2=="papel":
    print ("persona 2 gana! el papel envuelve a la piedra")
elif persona1=="piedra" and persona2=="tijera":
    print ("persona 1 gana! la piedra rompe la tijera")
elif persona1=="tijera" and persona2=="piedra":
    print ("persona 2 gana! la piedra rompe la tijera")
elif persona1=="tijera" and persona2=="papel":
    print ("persona 1 gana! la tijera corta el papel")   