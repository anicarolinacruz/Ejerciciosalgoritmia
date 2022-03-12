from ssl import VERIFY_ALLOW_PROXY_CERTS


compra=500000
porcentaje=0.12
descuento=(compra*porcentaje)
valor_pagar=compra-descuento
print("el descuento aplicado fue", descuento)
print("el total a pagar es", valor_pagar)
