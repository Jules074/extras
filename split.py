def main():
    texto = input('Texto: ')
    split_point = input('Split Point: ')

    separado = split(texto, split_point)
    print(separado)

def split(t,s):
    lista = []    
    temp = ''
    for i in t:
        if i == s:
            lista.append(temp)
            temp = ''
        else:
            temp += i
    lista.append(temp)
    
    return lista

main()