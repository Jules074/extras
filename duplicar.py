def main():
    palavra = input('Palavra: ')
    nova_palavra = duplicar(palavra)
    print(nova_palavra)
    
def duplicar(p):
    n = ''
    for i in p:
        n += i * 2

    return n

main()