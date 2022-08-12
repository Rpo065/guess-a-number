from random import randint

#Laço que permite sequência de jogos
while True:
    print("Bem vindo ao jogo ! Adivinhe o número sorteado!!")
    tentativa = 1
    sorteado = randint(0,100)
    chute = -1
    #Laço que permite sequência de tentativas
    while sorteado != chute:
        chute = int(input("Número sorteado: "))
        if chute > sorteado:
            print("O número sorteado é menor")
            tentativa+=1
        elif chute < sorteado:
            print("O número sorteado é maior")
            tentativa+=1
        else:
            print("Parabéns!!! Você acertou!!! \n")
            print(f"Parabéns!!! Você precisou de {tentativa} tentativas")
            tentativa = 0
    #Laço que para permitir somente o caracter válido    
    while True:
        resp = input("Deseja jogar novamente? Y / N \n").upper()
        if resp != "N" and resp != "Y":
            print("Informe Y para CONTINUAR e N para SAIR")
            continue
        else:
            break
        
    if resp == "Y":
        continue
    else:
        break

    
