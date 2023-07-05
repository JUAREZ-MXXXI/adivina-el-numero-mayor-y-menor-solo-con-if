# ingresar 5 numeros  y detectar el mayor y menor con if 
a1 = int(input("Ingrese el primer número: "))
b2 = int(input("Ingrese el segundo número: "))
c3 = int(input("Ingrese el tercer número: "))
d4 = int(input("Ingrese el cuarto número: "))
e5 = int(input("Ingrese el quinto número: "))

max = a1
min = a1

if b2 > max:
    max = b2
if c3 > max:
    max = c3
if d4 > max:
    max = d4
if e5 > max:
    max = e5

if b2 < min:
    min = b2
if c3 < min:
    min = c3
if d4 < min:
    min = d4
if e5 < min:
    min = e5

print("El número mayor es:", max)
print("El número menor es:", min)
