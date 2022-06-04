class Cuenta:
    def __init__(self, numero, fechaApertura, saldo):
        self.numero=numero
        self.fechaApertura=fechaApertura
        self.saldo=saldo
        
    def retiroCuenta(self):
        while True:
            self.retiro=int(input('digite el valor a retirar : '))
            if self.retiro>0 and self.retiro<=self.saldo:
                self.saldo-=self.retiro
                return f'Retiro Exitoso {self.saldo}'
            else:
                print (f'Cantidad insuficiente saldo disponible {self.saldo}')
                continue

    def Consingar(self):
        self.consignarCuenta=int(input('digite el valo a consignar : '))
        self.saldo+=self.consignarCuenta
        return f'consinar exitosas {self.saldo}'
    
    def getNumero(self):
        return self.numero
    
    def getFechaApertura(self):
        return self.fechaApertura
    
    def getSaldo(self):
        return self.saldo
    
    
    def obtenerInformacion(self):
        info="información de cuenta"
        info+="\nnumero:"+str(self.getNumero())
        info+="\nfecha Apertura:"+str(self.getFechaApertura())
        info+="\nsaldo:"+str(self.getSaldo())
        return info

class CuentaCorriente(Cuenta):
    
    def __init__(self, numero, fechaApertura, saldo, cheque):
        super().__init__(numero, fechaApertura, saldo)
        self.cheque=cheque
        
    def NumeroCheque(self):
        return f'su numero chequera es: {self.cheque}'
