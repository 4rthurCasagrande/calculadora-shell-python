# calculadora-shell-python

## Como executar o arquivo .sh
- Abra o terminal
- Navegue até o local onde o repositório foi baixado:
- E, no terminal, digite:
  "cd (pasta onde o arquivo foi baixado)"
- Ainda no terminal, para dar a permissão de execução do .sh, digite:
  "chmod 744 calculadora.sh"
- Por fim, para executar o script, digite:
  "./calculadora.sh"


## Explicação do código Python

Loop principal (while True)
Mantém o programa ativo até que o usuário escolha sair digitando 5.

Menu de operações
O usuário escolhe a operação desejada:

1 - Soma

2 - Subtração

3 - Multiplicação

4 - Divisão

5 - Sair

Entrada de números
Solicita dois números do usuário, convertendo para float para permitir decimais.

Execução das operações

Soma: num1 + num2

Subtração: num1 - num2

Multiplicação: num1 * num2

Divisão: num1 / num2, com checagem para não dividir por zero.

Saída
Exibe o resultado da operação no terminal usando print().

Validação de entradas
O código verifica se a operação escolhida é válida e se o usuário não tenta dividir por zero.
