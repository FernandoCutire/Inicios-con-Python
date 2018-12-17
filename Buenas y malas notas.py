## Buenas y malas notas

while(True)
print("Poner numeros decimales con '.' y no con ','")
nota = float(input("Introduce tu nota: "))
if nota > 4:
    print("Tienes una increible nota")
elif nota >= 3  :
    print("Estas pasando")
elif nota < 3:
    print("Te estas quedando")
else:
    print("Introduce un nuevo numero")