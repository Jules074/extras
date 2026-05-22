def main():
    acoes = []

    while True:
        menu = int(input('''
---------MENU---------
- 1: Adicionar Ação
- 2: Listar Ações
- 3: Remover Ação
- 4: Ações com Menor e Maior Preço
- 5: Empresa com maior investimento
- 6: Capital Total
- 0: Fechar Programa

>> '''))

        if menu == 0:
            break

        elif menu == 1:
            x = add_acao(acoes)
            if type(x) == list:
                acoes = x #substituir acoes por nova lista modificada
            else:
                print(x) #imprimir mensagem de erro
            
        elif menu == 2:
            for i in acoes:
                print(i)

        elif menu == 3:
            variavel = remover_acao(acoes)
            if type(variavel) == 'list':
                acoes = variavel
            else:
                for i in variavel:
                    print(i)

        elif menu == 4:
            print(menor_maior(acoes))

        elif menu == 5:
            print(maior_invest(acoes))

        elif menu == 6:
            print(capital_total(acoes))
        
def add_acao(a):
    acoes_temp = a
    acao = []

    empresa = input('Empresa: ')
    simbolo = input('Simbolo: ')
    valor = float(input('Valor: '))
    quantidade = int(input('Quantidade: '))
    
    if len(a) > 0:
        for i in a:
            variavel1 = anti_repeticao(i,empresa,simbolo)
            variavel2 = anti_valor_invalido(valor, quantidade)
            
        if variavel1 == 'safe' and variavel2 == 'safe': #não há repetição nem valores inválidos
            acao.append(empresa)
            acao.append(simbolo)
            acao.append(valor)
            acao.append(quantidade)

            acoes_temp.append(acao)

        elif variavel1 != 'safe':
            return variavel1
        elif variavel2 != 'safe':
            return variavel2
        
    else:
        variavel2 = anti_valor_invalido(valor,quantidade)
        if variavel2 != 'safe':
            return variavel2
        else:
            acao.append(empresa)
            acao.append(simbolo)
            acao.append(valor)
            acao.append(quantidade)

        acoes_temp.append(acao)

        return acoes_temp

def anti_repeticao(i,e,s):
    if e == i[0]:
        return 'Essa ação já foi cadastrada!'
    elif s == i[1]:
        return 'Essa ação já foi cadastrada!'
    else:
        return 'safe'
    
def anti_valor_invalido(v,q):
    if v <= 0:
        return 'Esse valor é inválido!'
    elif q <= 0:
        return 'Essa quantidade é inválida!'
    else:
        return 'safe'

def remover_acao(a):
    acoes_temp = a
    confirmador = 0
    simbolo_acao = input('Qual o Simbolo da ação que deseja remover?'
    '>> ')

    volta = 0
    for acao in acoes_temp:
        if acao[1] == simbolo_acao:
            acoes_temp.pop(volta)
            confirmador += 1
        volta += 1

    if confirmador == 0:
        return f'Não há ações registradas com esse simbolo: {simbolo_acao}.'
    else:
        return acoes_temp
    
def menor_maior(a):
    maior = a[0][3]
    empresa_maior = a[0][0]
    menor = a[0][3]
    empresa_menor = a[0][0]

    for acao in a:
        if acao[3] > maior:
            maior = acao[3]
            empresa_maior = acao[0]
        if acao[3] < menor:
            menor = acao[3]
            empresa_menor = acao[0]

    return f'''
Empresa com maior valor de investimento: {empresa_maior}, com R${maior}.
Empresa com menor valor de investimento: {empresa_menor}, com R${menor}.'''

def maior_invest(a):
    maior = 0
    empresa_maior = ''

    for acao in a:
        mult = acao[3] * acao[2]
        if mult > maior:
            maior = mult
            empresa_maior = acao[0]
    return f'''Empresa com maior investimento: {empresa_maior}, com R${maior} investido.'''

def capital_total(a):
    somatorio = 0

    for acao in a:
        mult = acao[3] * acao[2]
        somatorio += mult

    return f'''Capital Total das Ações: R${somatorio}'''

main()