while True:
  print("\nEscolha a operação que deseja realizar:\n")
  print("1 - Soma")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")
  print("5 - Sair\n")

  operacao = int(input())

  if operacao == 5:
    print("Programa encerrado!")
    break

  if operacao not in [1, 2, 3, 4]:
    print("Opção inválida. Tente novamente.")
    continue

  print("Digite o primeiro número:")
  num1 = float(input())
  print("Digite o segundo número:")
  num2 = float(input())

  if operacao == 1:
    print(f"O resultado da soma é: {num1 + num2}")
  elif operacao == 2:
    print(f"O resultado da subtração é: {num1 - num2}")
  elif operacao == 3:
    print(f"O resultado da multiplicação é: {num1 * num2}")
  elif operacao == 4:
    if num2 == 0:
      print("Não é possível dividir por zero.")
      continue
    print(f"O resultado da divisão é: {num1 / num2}")
