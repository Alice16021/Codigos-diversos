import numpy as np

# 1. Dados de Treinamento (x) e Respostas Corretas (y)
# Queremos que a IA aprenda a regra: y = 3 * x
X = np.array([[1.0], [2.0], [3.0], [4.0]]) # Entradas
Y = np.array([[3.0], [6.0], [9.0], [12.0]]) # Respostas reais

# 2. Inicialização dos Parâmetros (Pesos e Viés)
# Começamos com valores aleatórios chutados pela máquina
np.random.seed(42)
W = np.random.randn(1, 1)  # Matriz de Pesos (1x1)
b = np.zeros((1, 1))       # Vetor de Viés (Bias)

# Hiperparâmetros
taxa_aprendizado = 0.01
epocas = 500
n = X.shape[0] # Número de exemplos (4)

print(#9881;️ Inicializando o neurônio...)
print(f"Peso inicial: {W[0][0]:.4f} | Viés inicial: {b[0][0]:.4f}\n")

# Loop de Treinamento
for epoca in range(epocas):
    
    # ----------------------------------------------------
    # EQUAÇÃO 1: A Camada Linear (Forward Pass)
    # z = W*x + b
    # ----------------------------------------------------
    Z = np.dot(X, W) + b  # Multiplicação de matrizes + viés
    
    # ----------------------------------------------------
    # EQUAÇÃO 2: Função de Custo (Erro Quadrático Médio)
    # MSE = (1/n) * soma((y - chuto)^2)
    # ----------------------------------------------------
    erro = Z - Y
    custo = np.mean(erro ** 2)
    
    # ----------------------------------------------------
    # EQUAÇÃO 3: Descida do Gradiente (Backpropagation)
    # Calculando as derivadas parciais usando a Regra da Cadeia
    # ----------------------------------------------------
    # Derivada do custo em relação ao Peso (W)
    dW = (2 / n) * np.dot(X.T, erro)
    
    # Derivada do custo em relação ao Viés (b)
    db = (2 / n) * np.sum(erro, axis=0, keepdims=True)
    
    # Atualizando os pesos: W = W - alfa * dW
    W = W - taxa_aprendizado * dW
    b = b - taxa_aprendizado * db
    
    # Mostra o progresso a cada 100 passos
    if (epoca + 1) % 100 == 0:
        print(f"Época {epoca+1:03d} -> Erro (Custo): {custo:.6f} | Peso: {W[0][0]:.4f} | Viés: {b[0][0]:.4f}")

# 3. Testando o modelo treinado
print("\n#127891; Treinamento concluído!")
print(f"Peso final ideal (deveria ser 3): {W[0][0]:.4f}")
print(f"Viés final ideal (deveria ser 0): {b[0][0]:.4f}")

novo_x = np.array([[5.0]])
predicao = np.dot(novo_x, W) + b
print(f"\n#128302; Testando previsão para X=5: O neurônio chutou {predicao[0][0]:.4f} (Correto: 15.0)")
