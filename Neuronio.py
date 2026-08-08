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



import numpy as np

def treinar_neuronio(alvo: float, entrada: float = 1.0, taxa_aprendizado: float = 0.05, tolerancia: float = 0.01, max_epocas: int = 1000):
    """
    Treina um neurônio de peso único usando NumPy e Gradient Descent
    para prever um número alvo fornecido pelo usuário.
    """
    # Converter entradas para matrizes NumPy (estrutura de tensores)
    X = np.array([[entrada]], dtype=np.float64)
    Y = np.array([[alvo]], dtype=np.float64)
    
    # Inicializa o peso W aleatoriamente entre -10 e 10
    W = np.random.uniform(-10.0, 10.0)
    
    print(f"\n[+] Valor Alvo (Y): {alvo}")
    print(f"[+] Entrada fixa (X): {entrada}")
    print(f"[+] Peso Inicial Aleatório (W): {W:.4f}\n")
    print("-" * 65)
    print(f"{'Época':<10} | {'Previsão':<15} | {'Erro':<15} | {'Novo Peso':<15}")
    print("-" * 65)
    
    epocas_executadas = 0
    
    for epoca in range(1, max_epocas + 1):
        epocas_executadas = epoca
        
        # 1. Feedforward (Previsão)
        previsao = X * W
        
        # 2. Cálculo do Erro (Erro = Previsão - Alvo)
        erro = previsao - Y
        
        # Extrai os valores numéricos dos arrays NumPy
        val_previsao = previsao[0][0]
        val_erro = erro[0][0]
        
        # Critério de Parada: Se a diferença absoluta for menor que a tolerância
        if abs(val_erro) <= tolerancia:
            print(f"{epoca:<10} | {val_previsao:<15.4f} | {val_erro:<15.4f} | {W:<15.4f} [CONVERGIU!]")
            break
            
        # 3. Derivada e Atualização do Peso (Gradient Descent)
        # dL/dW = erro * X
        gradiente = val_erro * X[0][0]
        W = W - (taxa_aprendizado * gradiente)
        
        # Exibe o progresso a cada 5 épocas ou na primeira
        if epoca == 1 or epoca % 5 == 0:
            print(f"{epoca:<10} | {val_previsao:<15.4f} | {val_erro:<15.4f} | {W:<15.4f}")

    print("-" * 65)
    print(f"\n[✓] Treinamento concluído em {epocas_executadas} épocas!")
    print(f"[✓] Valor final estimado: {X[0][0] * W:.4f} (Objetivo era: {alvo})")

def main():
    print("=" * 50)
    print("   SINGLE-NEURON TARGET ESTIMATOR (NumPy Pure)")
    print("=" * 50)
    
    try:
        entrada_usuario = float(input("Digite o número que você quer que o neurônio adivinhe: "))
        treinar_neuronio(alvo=entrada_usuario)
    except ValueError:
        print("[!] Erro: Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
