## 🤖 Sistema de Paletização UR10
Este projeto implementa um sistema de paletização da receita de quadrado (1 layer) automatizado utilizando um braço robótico Universal Robots (UR10). O controle é realizado através de scripts URScript enviados via TCP/IP, com uma interface de monitoramento e comando rodando em um servidor Python externo.
## 📋 Visão Geral do Funcionamento
O sistema opera em uma arquitetura Cliente-Servidor:
### Servidor Python: Envia o script de controle para o robô, gerencia a lógica de comandos (STOP, PAUSE, MOVE) e recebe telemetria de tempo de ciclo.
### Robô (UR10): Executa a lógica de movimentação, calcula as posições de paletização via interpolação de poses e gerencia timers internos por meio de threads paralelas.
## 🛠️ Funcionalidades Principais
* Configuração Flexível de Pontos:
Modo FIXO: Utiliza coordenadas pré-configuradas no código.Modo ALTERAR: Permite que o operador use o Freedrive para ensinar os 4 cantos do palete em tempo real.
* Cálculo Dinâmico de Grade: O robô calcula automaticamente a posição de cada caixa em uma grade de (6 caixas) utilizando a função interpolate_pose.
* Monitoramento de Performance: Threads dedicadas contam os ciclos de clock do controlador para calcular o tempo exato de cada ciclo e de cada caixa individualmente em segundos.
* Controle Remoto via Terminal: Envio de comandos em tempo real como interrupção de emergência ou movimentação manual para pontos específicos.
* Blend entre os movimentos do robô
* Mudar a orientação das caixas em cada camada 
