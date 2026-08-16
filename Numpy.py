import numpy as np

#(X = entrada, Y = resposta real)
X = np.array([[2.0]])
Y = np.array([[200.0]])

#Chute inicial
W = 10.0
taxa_aprendizado = 0.1

print(f"Peso Inicial: {W}")

#10 épocas (iterações)
for epoca in range(1, 11):
    # Previsão 1
    previsao = X * W
    
    # Erro 1
    erro = previsao - Y
    
    # Atualização do peso (taxa de aprendizado)
    # Erro do array usando [0][0] apenas para exibir como número limpo
    W = W - (taxa_aprendizado * erro[0][0] * X[0][0])
    
    print(f"Época {epoca} -> Previsão: {previsao[0][0]:.1f} | Erro: {erro[0][0]:.1f} | Novo Peso: {W:.1f}")
