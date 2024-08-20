import os
#1
print("Ejercicio 1")
num=int(input("Ingrese un número "))
if num > 0:
    print("El número es positivo")
elif num==0:
    print("El número es 0")
else:
    print("El número es negativo")
    
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#2
print("Ejercicio 2")
num1=int(input("Ingrese un número "))
if num1 > 5:
    num1 = num1*2
    print("Su número:",num1)
elif num1 == 5:
    print("Número 5")
else:
    num1 = num1*3
    print("Su número",num1)
    
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#3
print("Ejercicio 3")
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
    
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#4
print("Ejercicio 4")
edad=int(input("Ingrese su edad (0 a 100 años) "))
while edad<0 or edad > 100:
    edad=int(input("Ingrese edad válida (0 a 100 años) "))
if edad >= 20:
    if edad >=20 and edad <=39:
        print("Su categoría es ADULTO")
    elif edad >= 40 and edad <= 60:
        print("Su categoría es MAYOR")
    elif edad > 60:
        print(print("Su categoría es TERCERA EDAD"))
else:
    print("Su categoría es JOVEN")
    
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#5
print("Ejercicio 5")
num1=float(input("Ingrese el primer número "))
num2=float(input("Ingrese el segundo número "))
num3=float(input("Ingrese el tercer número "))
num4 =float(input("Ingrese el cuarto número "))
suma1=num1+num2
suma2=num3+num4
if suma1>suma2:
    print("La suma de los primeros dos números",suma1,"es mayor a la suma de los últimos dos",suma2)
else: 
    print("La suma de los últimos dos números",suma2,"es mayor a la suma de los primeros dos",suma1)
    
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#6
print("Ejercicio 6")
numero=float(input("Ingrese un número "))
numero1=float(input("Ingrese otro número "))
suma=numero+numero1
if suma>0:
    print("La suma de los números es positivo")
elif suma==0:
    print("La suma de los dos números da 0")
else: 
    print("La suma de los dos números es negativo")
    
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#7
print("Ejercicio 7")
nota1=int(input("Ingresar la primera nota "))
while nota1 < 0 or nota1 > 10:
    nota1=int(input("Ingresar nota válida "))
nota2=int(input("Ingresar la segunda nota "))
while nota2 < 0 or nota2 > 10:
    nota2=int(input("Ingresar nota válida "))
nota3=int(input("Ingresar la tercera nota "))
while nota3 < 0 or nota3 > 10:
    nota3=int(input("Ingresar nota válida "))
promedio=(nota1+nota2+nota3)/3
if promedio >= 4:
    if promedio >= 4 and promedio < 7:
        print("Aprobado")
    elif promedio >=7:
        print("Promovido")
else:
    print("Aplazado")
    
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#8
print("Ejercicio 8")
n1=float(input("Ingresar primer número "))
n2=float(input("Ingresar segundo número "))
if n1 < n2:
    print("Está en orden CRECIENTE")
elif n1 == n2:
    print("Los números son iguales")
else:
    print("Está en orden DECRECIENTE")
    
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#9
print("Ejercicio 9")
categoria=int(input("Ingresar la categoría del trabajador "))
while categoria < 0 or categoria > 4:
    categoria=int(input("Ingresar categoría válida (entre 1 y 4) "))
sueldo=float(input("Ingresar el sueldo actual del trabajador "))
if categoria < 1:
    print("")
elif categoria==2:
    aumento=((sueldo*10)/100)+sueldo
    print("El sueldo con aumento del trabajador será de $",aumento)
elif categoria==3:
    aumento=((sueldo*8)/100)+sueldo
    print("El sueldo con aumento del trabajador será de $",aumento)
elif categoria==4:
    aumento=((sueldo*7)/100)+sueldo
    print("El sueldo con aumento del trabajador será de $",aumento)
else:
    aumento=((sueldo*15)/100)+sueldo
    print("El sueldo con aumento del trabajador será de $",aumento)