## P-adic metric ##

# Función que verifica si un número es primo
# Si es primo: retorna True
# Si NO es primo: retorna Falso
def esPrimo(n):
    n = abs(int(n)) # n debe ser un entero positivo

    if n < 2:
        return False 

    if n == 2:
        return True

    if not n & 1: # n es par
        return False

    for x in range(3, int(n ** 0.5)+ 1, 2):
        if n % x == 0:
            return False # n es divisible por alguno de los números comprendidos entre 3 y n^0.5

    return True


# Función que retorna la valuación p-ádica de un número x en el número p.
def valuacion_p_adica(x, p):
    # x: el número a ser evaluado.
    # p: el número primo.
    # Return: la valuación p-ádica de x en p.

    # Inicializamos la valuación p-ádica de x en p.
    v = 0 
    while x % p == 0: # x es divisible por p.
        x = x // p # x // p es el cociente de x entre p.
        v += 1 # Incrementamos la valuación p-ádica de x en p.

    return v 


# Retorna el valor absoluto de x en p.
# x: el número a ser evaluado.
# p: el número primo.
abs_p_adico = lambda x, p: 1 / (p ** (valuacion_p_adica(x, p)))


# Función que retorna la distancia/métrica p-ádica entre dos números x e y, en el número p.
def metrica_p_adica(a, b, p):
    # Calculamos la distancia p-ádica entre a y b, en el número p.
    # a: el primer número.
    # b: el segundo número.
    # p: el número primo.

    if not esPrimo(p): # Verificammos si p es primo.
        print(f"[ ! ] {p} debe ser primo.")
        return None
    
    # Verificamos que x sea un número positivo.
    if a < 0 or b < 0:
        print(f"[ ! ] {a} y {b} deben ser números positivos.")
        return None
        
    # Calculamos la distancia p-ádica entre a y b, en el número p.
    return abs_p_adico(a - b, p)

def main():
    # Calculamos la distancia p-ádica entre a y b, en el número p.
    a = int(input("Ingrese el primer número:\n> "))
    b = int(input("Ingrese el segundo número:\n> "))
    p = int(input("Ingrese el número primo:\n> "))

    print(f"La distancia p-adica entre {a} y {b} en el número {p} es: {metrica_p_adica(a, b, p)}")

if __name__ == "__main__":
    main()
