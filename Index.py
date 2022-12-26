menu = '''
================ Opções ================


[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> '''
saldo = 0
limite = 500
extrato = " "
num_saques = 0
LIMITE_SAQUES = 3


opcao = input(menu)
while True:
    
    if opcao == "1":
        valor = float(input(" Digite o valor Desejado => "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor: .2f}\n"
        
        else:
            print("Operação Falhou. Valor Digitado inválido.")

    elif opcao == '2':
        valor = float(input("Informe o Valor de saque => "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque_limite = num_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou. Você não possui saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou. Você está tentando sacar mais do que o limite permite.")
       
        elif excedeu_saque_limite:
            print("Saque máximo diário atingido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor: .2f}\n"
            num_saques += 1
        
        else:
            print("Operação Falhou. Valor inválido.")

    elif opcao == "3":
        print ('//////////////////////// EXTRATO /////////////////////////////')
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo R$ {saldo: .2f} ")
        print("==================================================================") 

    elif opcao == "4":
        break

    else:
        print("Opção Inválida")
        
    opcao = input(menu)
