def main():
    texto = input('Texto: ')
    caractere = input('Caractere: ')
    substituto = input('Caractere substituto: ')

    novo = swapper(texto, caractere, substituto)
    print(novo)

def swapper(t, c, s):
    novo_texto = ''
    for i in t:
        if i == c:
            novo_texto += s
        else:
            novo_texto += i
    
    return novo_texto

main()