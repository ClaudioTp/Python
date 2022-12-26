saldo:1500
saque:500
cheque_especial : 100
conta_normal : True



if conta_normal:
	if saldo >= saque:
		print("Saque realizado com sucesso!")
	elif saque <= (saldo + cheque_especial):
		print("Saque realizado com uso do cheque especial!")
