import random

def main():
    num_secreto = random.randint(1, 100)

    chutes = 10
    pontos = 100
    guess = int(input('Eu tenho um numero... qual numero será esse? '))

    while chutes >= 0:
        if guess == num_secreto:
            chutes -= 1
            print(f'você acertou! O numero é {num_secreto}, acertou após {10 - chutes} chutes\nVOCE TEM {pontos} PONTOS')
            break
        elif guess > num_secreto:
            print('errou! seu numero está acima do numero...')
            chutes -= 1
            pontos -= 10
            guess = int(input('Eu tenho um numero... qual numero será esse? '))
        elif guess < num_secreto:
            print('errou! seu numero está abaixo do numero...')
            chutes -= 1
            pontos -= 10
            guess = int(input('Eu tenho um numero... qual numero será esse? '))
        if chutes == 0:         
            print('acabaram as chances, PERDEU BELELEU')
            break


main()