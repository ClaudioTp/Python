md1 = int(input("Qual a Nota da sua primeira Prova:  "))
md2 = int(input("Qual a Nota da sua segunda Prova:  "))
md3 = int(input(" Qual a Nota da Sua terceira prova:  "))
md4 = int(input("qual a nota da sua quarta prova:  "))

media_final = (md1 + md2 +md3 + md4) / 4

print("{:,.1f}".format(media_final))

if media_final < 5 :
    print("reprovado")
elif media_final > 5 and media_final <= 7 :
    print("Aprovado com Recuperçao")
elif media_final == 8 :
    print("Aprovado\n PARABENS!!!")
elif media_final == 9 :
    print("Aprovado com distinçao")
else:
    print("Seu Futuro esta Garantido")