import numpy as np

# Nossos dados do papel (X = entrada, Y = resposta real)
X = np.array([[2.0]])
Y = np.array([[200.0]])

# Chute inicial que demos no papel
W = 10.0
taxa_aprendizado = 0.1

print(f"Peso Inicial: {W}")

# Vamos rodar 10 épocas (iterações)
for epoca in range(1, 11):
    # 1. Previsão (Exatamente o que você calculou: Previsão = 92 no passo 2)
    previsao = X * W
    
    # 2. Erro (Exatamente o que você calculou: Erro = -108 no passo 2)
    erro = previsao - Y
    
    # 3. Atualização do Peso (A fórmula que usamos com a taxa de aprendizado)
    # Pegamos o erro do array usando [0][0] apenas para exibir como número limpo
    W = W - (taxa_aprendizado * erro[0][0] * X[0][0])
    
    print(f"Época {epoca} -> Previsão: {previsao[0][0]:.1f} | Erro: {erro[0][0]:.1f} | Novo Peso: {W:.1f}")
