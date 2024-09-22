#Parámetros y retorno de valores en funciones

#Función calcular descuento
def calcular_descuento (monto,porcentaje=10):
    descuento= monto*(porcentaje/100) #calculo del descuento de compra
    return descuento #retorno de la función

monto_compra=float(input("Ingrese el monto total de la compra: ")) #Monto de compra 1
descuento_compra=calcular_descuento(monto_compra) #Llamado a la función
total_pagar=monto_compra-descuento_compra #Calculo del total a pagar
print(f"Monto de descuento={descuento_compra:.2f}\nTotal a pagar={total_pagar:.2f}\n")

monto_compra=float(input("Ingrese el monto total de la compra: ")) #Monto de compra 2
porcentaje_descuento=int(input("Ingrese el porcentaje de descuento de la compra: ")) #Porcentaje de descuento
descuento_compra=calcular_descuento(monto_compra,porcentaje_descuento) #Llamado a la función
total_pagar=monto_compra-descuento_compra #Calculo del total a pagar
print(f"Monto de descuento={descuento_compra:.2f}\nTotal a pagar={total_pagar:.2f}")