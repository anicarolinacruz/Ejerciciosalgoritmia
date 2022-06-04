import cuenta

cuenta1 =cuenta.Cuenta(12345,'13-2-2022',5000)
print(cuenta1.retiroCuenta())
print(cuenta1.Consingar())
print(cuenta1.obtenerInformacion())

cuentaCorriente=cuenta.CuentaCorriente(2345,'13-04-2022',10000,1410)
print(cuentaCorriente.retiroCuenta())
print(cuentaCorriente.Consingar())
print(cuentaCorriente.obtenerInformacion())
print(cuentaCorriente.NumeroCheque())
