def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a / b

while True:
    print("Bienvenido a mi calculadora.....")    
    while True:

        try:
            numerouno = float(input("ingrese el primer numero: "))
            break
        except ValueError:
            print("usted ingreso un valor no valido")
    
    operador = (input("ingrese el operador (opciones: +,-,*,/):"))
    
    while True:
        try:
            numerodos = float(input("ingrese el segundo numero: "))
            break
        except ValueError:
            print("usted ingreso un valor no valido")

    if operador =="+":
        resultado = suma(numerouno, numerodos)
        print(numerouno, operador, numerodos, "=", resultado)
    elif operador =="-":
        resultado = resta(numerouno,numerodos)
        print(numerouno, operador, numerodos, "=", resultado)
    elif operador =="*":
        resultado = multiplicacion(numerouno,numerodos)
        print(numerouno, operador, numerodos, "=", resultado)
    elif operador =="/":
        resultado = division(numerouno,numerodos)
        print(numerouno, operador, numerodos, "=", resultado)
    else:
        print("usted ingreso un operador no valido, intente denuevo")
    
    
