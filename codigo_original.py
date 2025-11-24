import time

def es_primo(n):
    if n <= 1: return False
    # Ineficiencia: Itera hasta n (O(n))
    for i in range(2, n):
        if n % i == 0: return False
    return True

def buscar_primos(limite):
    primos = []
    for num in range(1, limite + 1):
        if es_primo(num):
            primos.append(num)
    return primos

if __name__ == "__main__":
    # La actividad pide hasta 100,000
    LIMITE = 100000 
    
    print(f"Buscando primos hasta {LIMITE} (Método Original)...")
    inicio = time.time()
    buscar_primos(LIMITE)
    fin = time.time()
    
    print(f"Tiempo Original: {fin - inicio:.4f} segundos")