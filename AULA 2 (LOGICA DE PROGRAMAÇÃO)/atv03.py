idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
    exit()


habilitação = int(input("Você possui habilitação? (DIGITE 1 PARA SIM e 2 PARA NÂO): "))

if habilitação == 1:
    print("Você possui habilitação")
elif habilitação == 2:
    print("Você não possui habilitação")
else:
    print("Digite uma resposta validada")
