
#!/bin/bash

#Visualização no terminal
VERDE="\033[0;32m"
AZUL="\033[0;34m"
SEM_COR="\033[0m"

echo -e "${AZUL}=========================================${SEM_COR}"
echo -e "${VERDE}   TOOLKIT DE RECONHECIMENTO INICIAL     ${SEM_COR}"
echo -e "${AZUL}=========================================${SEM_COR}"

# Solicita o alvo ao usuário
read -p "Digite o IP ou URL do alvo: " ALVO

echo -e "\n${AZUL}[*] Iniciando Host Discovery (Ping Sweep)...${SEM_COR}"
nmap -sP "$ALVO"

echo -e "\n${AZUL}[*] Testando conectividade com NPing...${SEM_COR}"
nping --echo-client "public" "$ALVO" -c 2

echo -e "\n${AZUL}[*] Iniciando Scanner Agressivo (Versões e SO)...${SEM_COR}"
echo "Isso pode levar alguns minutos..."
nmap -sV -A "$ALVO"

echo -e "\n${VERDE}[!] Varredura concluída para: $ALVO ${SEM_COR}"
