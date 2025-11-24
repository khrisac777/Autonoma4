import time
import numpy as np

# Optimización 1: Reducir el rango del bucle (Raíz Cuadrada) [cite: 44]
def es_primo_raiz(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    # Iterar solo hasta la raíz cuadrada + 1, saltando pares
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

# Optimización 2: List Comprehensions [cite: 45]
def buscar_primos_list_comp(limite):
    return [num for num in range(1, limite + 1) if es_primo_raiz(num)]

# Optimización 3: NumPy (Criba de Eratóstenes Vectorizada) [cite: 46]
def buscar_primos_numpy(limite):
    # Crear array de booleanos (True) para representar números
    es_primo = np.ones(limite + 1, dtype=bool)
    es_primo[:2] = False # 0 y 1 no son primos
    n_max = int(np.sqrt(limite)) + 1
    
    for i in range(2, n_max):
        if es_primo[i]:
            # Vectorización: marcar todos los múltiplos de i como False de golpe
            es_primo[i*i:limite+1:i] = False
    
    # Retornar los índices que quedaron como True
    return np.nonzero(es_primo)[0]

if __name__ == "__main__":
    LIMITE = 100000
    
    print(f"--- Optimizando para N={LIMITE} ---")
    
    # Prueba 1: Python Optimizado (Raíz + List Comp)
    inicio = time.time()
    primos_py = buscar_primos_list_comp(LIMITE)
    fin = time.time()
    print(f"Tiempo Python Optimizado: {fin - inicio:.4f} seg")

    # Prueba 2: NumPy
    inicio = time.time()
    primos_np = buscar_primos_numpy(LIMITE)
    fin = time.time()
    print(f"Tiempo NumPy (Vectorizado): {fin - inicio:.4f} seg")