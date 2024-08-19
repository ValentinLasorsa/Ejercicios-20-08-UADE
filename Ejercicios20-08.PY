#1
"""
num=int(input("Ingrese un número "))
if num > 0:
    print("El número es positivo")
elif num==0:
    print("El número es 0")
else:
    print("El número es negativo")

#2
num1=int(input("Ingrese un número "))
if num1 > 5:
    num1 = num1*2
    print("Su número:",num1)
elif num1 == 5:
    print("Número 5")
else:
    num1 = num1*3
    print("Su número",num1)
"""
#3
Nota=int(input("Ingrese la nota del alumno (entre 0 y 100): "))
while Nota<0 or Nota>100:
    Nota=int(input("Ingrese una nota válida (entre 0 y 100): "))
if Nota>=69:
    if Nota>=90:
        print("Al alumno le queda una A")
    elif Nota<90 and Nota>=80:
        print("Al alumno le queda una B")
    elif Nota<80 and Nota>=70:
        print("Al alumno le queda una C")
    elif Nota<70 and Nota>=69:
        print("Al alumno le queda una D")
else:
    print("Al alumno le queda una E")