from random import randint

print('♦ Hello ♦')
print('''Sou o seu computador...
Acabei de pensar num número entre 0 e 10.
Será que vc consegue adivinhar?''')
computador = randint(0,10)
acertou = False
palpites = 0

while not acertou:
    jg = int(input('Que número eu pensei? '))
    palpites += 1
    if jg == computador:
        acertou = True
    else:
        if jg < computador:
            print('Hmm... quase lá, tente um número maior')
        elif jg > computador:
            print('Hmm...a ainda não, tente um número menor')
print('Parabéns !! eu realmente tinha pensando no {}'.format(computador))


        

