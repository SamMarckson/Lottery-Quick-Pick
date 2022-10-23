import random
jogos = list()
numSorteados = list()

tam = 0;
qtd = int(input("Quantos jogos serão gerados? "))

while tam<qtd:
    cont = 0
    while True:
        num = random.randint(1,60)
        if num not in numSorteados:
           numSorteados.append(num)
           cont += 1
        if cont >= 6:
            break
    numSorteados.sort()
    print(f"Os numeros sorteados foram {numSorteados}")
    jogos.append(numSorteados[:])
    numSorteados.clear()
    tam += 1

print("=-"*30*qtd)
print(f"A lista completa eh: {jogos}")



