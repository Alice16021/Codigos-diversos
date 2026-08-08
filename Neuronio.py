import numpy as np
def neuronio (alvo: float, entrada: float=1.0, taxa_aprendizagem:float=0.05, tolerancia:float=0.01, max_epocas:1000):

    X=np.array([[entrada]], dtype=np.float64)
    Y=np.array([[alvo]], dtype=np.float64)

    W=np.random.uniform(-10.0, 10.0)

    print(f"\n[+] Valor Alvo:{alvo}")
    print(f"[+] Entrada fixa: {entrada}")
    print(f"[+] Peso inicial aleatório: {W:.4f}\n")
    print("-"*65)
    print(f"{Epoca:<10}; ")
