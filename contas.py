conta_normal = True
saldo = 5000
cheque_especial = 200
conta_black = True


print('Escolha uma Opçoao')
print("[1] Saque ")
print("[2] Deposito")
print("[3] Extrado")
print("[4] Transferencia")

opçao = input()

if opçao == "1":
    print("Transferindo para saque\n escolha o Tipo da sua Conta")
if opçao == "2":
    print("Transferindo para Depositos\n escolha o Tipo da sua Conta")
if opçao == "3":
    print("Escolha sua conta\n Sera Exibido na tela o extrato")
else:
    print("Escolha sua conta\n")



print("Escolha uma Opçao")
print("\t[1]Conta Normal ")
print("\n\t[2]Conta Black  ")

opçao = input()
saque = int(input("Insira o valor do saque desejado: "))



if opçao == "1" and conta_normal :
        if saldo >= saque:
            print(" Saque realizado")
elif saque <= (cheque_especial + saldo):
        print(" Saque relaizado com uso do Cheque especial")
else:
        print(" Nao foi possivel realizar a operaçao...\n\t Motivo\n \tSaldo Insuficiente")
if opçao == "2" and conta_black:
    if saldo >= saque:
        print("Saque relaizado com sucesso")
    else:
        print("Saldo Insuficiente")
