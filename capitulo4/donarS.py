edad=int(input("ingrese edad: "))
peso=float(input("ingrese peso: "))
pulso=int(input("ingrese pulso por minuto: "))
plaquetas=float(input("ingrese plaquetas: "))

if edad>=18<=65 and peso>=50 and pulso>=50<=110 and plaquetas>=150.000:
    print("es apto para donar sangre")
else:
    print("no es apto para donar sangre")