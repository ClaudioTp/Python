A = float(input("Digite o Valor da Base A : "))
B = float(input("Digite o Valor da Base B: "))
C = float(input("Digite o Valor da altura: "))
 
if A >= 0 and B >= 0 and C >= 0 : 
    area =(A + B) * C /2
    print('A area É %.1f' %(area)) 
else:
    print("Nao Foi Possivel Calcular")