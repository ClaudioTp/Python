menu = '''
================ Opções: ================


[1] Depositar:
[2] Sacar:
[3] Extrato:
[4] Sair:

=> '''
saldo = 0
limite = 500
extrato = " "
numer_saques = 0
LIMITE_SAQUES = 3

opcao = input(menu)
while True:

    if opcao == "1":

        valor = float(input(" Digite o valor Desejado => "))

        if valor > 0:
            saldo += valor
            extrato += f"Depositado: r$ {valor: .2f}\n"
        
        else:
            print("Operaçao Falhou valor Digitado invalido")

    elif opcao == '2':
        valor = float(input("Informe o Valor desejado => "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque_limite = numer_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operaçao Falhou. Voçe Nao possui saldo suficiente")
       
        elif excedeu_limite:
            print("Operaçao falhou. Voçe esta tentanto sacara mais que o limite permite")
        
        elif excedeu_saque_limite:
            print("Saque maximo diario atingido")

        elif valor > 0 :
            saldo -= valor
            extrato += f"Saque R$ {valor: .2f}\n"
            numer_saques += 1
    
        else:
            print("Operaçao Falhou valor Invalido")



    elif opcao == "3" :
        print ('//////////////////////// EXTRATO /////////////////////////////')
        print("Nao Foram realizada movimentaçoes " if not extrato else extrato)
        print(f"\n Saldo R${saldo: .2f} ")
        print("==================================================================") 
       

    elif opcao == "4":
        break
    
    else :
        print("Opçao Invalida")

    opcao = input(menu)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     
