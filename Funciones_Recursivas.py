# Programación I - Funciones Recursivas

# Función auxiliar get_int (usada en el ejercicio 4)

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int:
    for intento in range(reintentos):
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(mensaje_error)
        except ValueError:
            print(mensaje_error)
    raise ValueError(f"Se superó el número máximo de reintentos ({reintentos}).")



# Ejercicio 1: Suma de los primeros N números naturales
# Ejemplo: sumar_naturales(5) = 1+2+3+4+5 = 15

def sumar_naturales(numero: int) -> int:
    if numero <= 0: # Caso base
        return 0
    return numero + sumar_naturales(numero - 1)


# Ejercicio 2: Potencia de un número (base ^ exponente)
# Ejemplo: calcular_potencia(2, 4) = 16

def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0: # Caso base: cualquier número ^ 0 = 1
        return 1
    return base * calcular_potencia(base, exponente - 1)


# Ejercicio 3: Suma de los dígitos de un número
# Ejemplo: sumar_digitos(1234) = 1+2+3+4 = 10

def sumar_digitos(numero: int) -> int:
    numero = abs(numero)    # Manejo de negativos
    if numero < 10:         # Caso base: un solo dígito
        return numero
    return (numero % 10) + sumar_digitos(numero // 10)


# Ejercicio 4: Número de Fibonacci
# F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)

def calcular_fibonacci(numero: int) -> int:
    if numero == 0: # Caso base 1
        return 0
    if numero == 1: # Caso base 2
        return 1
    return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)


# Ejercicio 1: Suma de los primeros N números naturales
# Ejemplo: sumar_naturales(5) = 1+2+3+4+5 = 15
numero = int(input("Ingresá un número: "))
resultado = sumar_naturales(numero)
print(f"Resultado: {resultado}")


# Ejercicio 2: Potencia de un número (base ^ exponente)
# Ejemplo: calcular_potencia(2, 4) = 16
base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente: "))
resultado = calcular_potencia(base, exponente)
print(f"Resultado: {resultado}")


# Ejercicio 3: Suma de los dígitos de un número
# Ejemplo: sumar_digitos(1234) = 1+2+3+4 = 10
numero = int(input("Ingresá un número: "))
resultado = sumar_digitos(numero)
print(f"Resultado: {resultado}")


# Ejercicio 4: Número de Fibonacci
# F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)
numero = int(input("Ingresá un número: "))
resultado = calcular_fibonacci(numero)
print(f"Resultado: {resultado}")


# Programa principal - Prueba de todas las funciones
if __name__ == "__main__":

    # Ejercicio 1 
    print("=" * 40)
    print("EJERCICIO 1: Suma de naturales")
    n = 5
    print(f"sumar_naturales({n}) = {sumar_naturales(n)}")   # 15

    # Ejercicio 2
    print("=" * 40)
    print("EJERCICIO 2: Potencia")
    base, exp = 2, 8
    print(f"calcular_potencia({base}, {exp}) = {calcular_potencia(base, exp)}")  # 256

    # Ejercicio 3
    print("=" * 40)
    print("EJERCICIO 3: Suma de dígitos")
    num = 1234
    print(f"sumar_digitos({num}) = {sumar_digitos(num)}")   # 10

    # Ejercicio 4
    print("=" * 40)
    print("EJERCICIO 4: Fibonacci")
    try:
        numero = get_int(
            mensaje="Ingresá un número para calcular Fibonacci (0-20): ",
            mensaje_error="Error: ingresá un número entero entre 0 y 20.",
            minimo=0,
            maximo=20,
            reintentos=3
        )
        print(f"calcular_fibonacci({numero}) = {calcular_fibonacci(numero)}")
    except ValueError as e:
        print(f"Error: {e}")