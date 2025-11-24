import cProfile
import pstats
import matplotlib.pyplot as plt
import codigo_original
import codigo_optimizado
import time

def run_analysis():
    LIMITE = 100000 
    
    print("1. Ejecutando Profiling...")
    profiler = cProfile.Profile()
    profiler.enable()
    codigo_original.buscar_primos(LIMITE)
    profiler.disable()
    
    with open("profiling_optimizado.txt", "w") as f:
        stats = pstats.Stats(profiler, stream=f)
        stats.strip_dirs().sort_stats('cumtime').print_stats(15)

    print("2. Midiendo tiempos para gráfico...")
    # Original
    t0 = time.time()
    codigo_original.buscar_primos(LIMITE)
    t_orig = time.time() - t0
    
    # Python Optimizado
    t1 = time.time()
    codigo_optimizado.buscar_primos_list_comp(LIMITE)
    t_opt = time.time() - t1
    
    # NumPy
    t2 = time.time()
    codigo_optimizado.buscar_primos_numpy(LIMITE)
    t_np = time.time() - t2

    print(f"Tiempos: Orig={t_orig:.4f}s, Opt={t_opt:.4f}s, Numpy={t_np:.4f}s")

    # Gráfico
    plt.figure(figsize=(10,6))
    plt.bar(['Original', 'Optimizado', 'NumPy'], [t_orig, t_opt, t_np], color=['red','orange','green'])
    plt.title(f"Comparativa de Tiempos (N={LIMITE})")
    plt.ylabel("Segundos")
    plt.savefig("grafico_tiempos.png")
    print("Gráfico guardado.")

if __name__ == "__main__":
    run_analysis()