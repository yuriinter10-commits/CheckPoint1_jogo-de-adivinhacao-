import random
palpite = 0
tentativas = 0

numero=secreto = random.randint(1,100)

while True: 
    
    palpite = int(input("Digite seu palpite: "))

    if palpite == secreto:
        print("Voce acertou: ")
        break
    elif palpite > secreto:
        print("Digite um numero menor!!! ")
    
    else:
        print("digite um numero maior!!! ")

    tentativas += 1

