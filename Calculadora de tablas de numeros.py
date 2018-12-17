## CALCULADORA DE TABLAS 

print("Esta calculadora puede sacar la tabla de cualquier numero")
a = int(input("Introduce un numero: "))
def dibujar_tabla_del_numero_indicado():
    for i in range(10):
        print(a," * {} = {}".format(i,i*a))
dibujar_tabla_del_numero_indicado()
