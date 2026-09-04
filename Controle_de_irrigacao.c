#include <stdio.h>
#include <stdbool.h>

const int PINO_SENSOR_UMIDADE=0;
const int PINO_BOMBA_AGUA=13;

const int LIMITE_UMIDADE_SECA=30;

int main() {
    printf("SISTEMA: CONTROLE DE IRRIGACAO \n");
    printf("Lendo sensores \n");

  //Leitura hipotética de sensores
  
    int leituraSolo[4]={65, 42, 25, 55};
    bool bombaLigada=false;
    
    for (int i=0; i<4; i++){
        int umidadeAtual=leituraSolo[i];
        
        printf("[Leituras #%d] Umidade detectada: %d%%\n", i+1, umidadeAtual);
        
        if (umidadeAtual<LIMITE_UMIDADE_SECA){
            bombaLigada=true;
            printf("Solo seco! Ligando pino %d.\n",PINO_BOMBA_AGUA);
            printf("status:[BOMBA D AGUA LIGADA]\n");
        }
        else {
            bombaLigada=false;
            printf("->Solo úmido. Desligando pino %d.\n", PINO_BOMBA_AGUA);
        }
        printf("Fim do programa. \n");
    }
    return 0;
}
