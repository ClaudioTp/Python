opçao = -1

while opçao != 0 :
    opçao= int(input(" [1] Sacar\n [2] Depositar\n [0] Sair\n: "))

    if opçao == 1:
        print("Sacando dinheiro")
    elif opçao == 2:
        print(int(input("Digite o valor de saque")))
    else :
        print("Saindo")