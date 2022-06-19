#14. A matriz a seguir mostra o custo unitário de cada produto e a quantidade de cada um
# dos produtos no estoque de três lojas de uma rede. Escreva um programa que exiba na tela as respostas para as perguntas.
# Na solução desse problema, elabore uma maneira de armazenar seus dados utilizando lista e sublistas. Os dados da matriz devem ser lidos do teclado.
#índice 0(produto 1)- indice 1(produto 2) - x 2 (produto 3) - x 3 (produto 4)
#índice 0(custo unitário) - índice 1 (loja 1) - y 2 (loja 2) - y 3(loja 3)
prod = ['A', 'B', 'C', 'D']
loja = [0, 1, 2, 3]
matriz = [[0 for z in range(4)] for z in range(4)]
while True:
    try:
        for x in range(4):
            matriz[x][0] = float(input(f'Digite custo unitário do produto {prod[x]}: '))
            for y in range(1, 4):
                matriz[x][y] = int(input(f'Digite o estoque da loja {loja[y]}: '))
    except:
        print('Impossivel digitar caracteres!\n'
              'somente valores!\n')
        continue
    for x in range(4):
        print('|R$',end='')
        for y in range(4):
            print(f' {matriz[x][y]} |', end='')
            if y == 3:
                lin = 30 * '─'
                print('\n',lin)
    break
while True:
    try:
        P = input('Quer saber mais detalhes da rede?\n'
              'S - sim\n'
              'N - não\n'
              '>> ')
        while P == 's' or P == 'S':
            pesq = int(input('1 - Valor total de estoque em cada uma das lojas?\n'
                         '2 - Valor total de estoque para cada produto disponível na rede?\n'
                         '3 - Valor total de estoque da rede?\n'
                         '>> '))
            if pesq == 1:
                l1 = 0
                l2 = 0
                l3 = 0
                for x in range(4):
                    l1 += matriz[x][1]
                    l2 += matriz[x][2]
                    l3 += matriz[x][3]
                print(f'total de estoque da loja 1 = {l1}')
                print(f'total de estoque da loja 2 = {l2}')
                print(f'total de estoque da loja 3 = {l3}')
            elif pesq == 2:
                pa = 0
                pb = 0
                pc = 0
                pd = 0
                for x in range(4):
                    for y in range(1, 4):
                        if x == 0:
                            pa += matriz[x][y]
                        elif x == 1:
                            pb += matriz[x][y]
                        elif x == 2:
                            pc += matriz[x][y]
                        elif x == 3:
                            pd += matriz[x][y]
                        else:
                            continue
                print(f'Estoque do produto A na rede é = {pa}\n'
                      f'Estoque do produto B na rede é = {pb}\n'
                      f'Estoque do produto C na rede é = {pc}\n'
                      f'Estoque do produto D na rede é = {pd}\n')
            elif pesq == 3:
                print(f'Estoque total na rede é = {pa + pb + pc +pd}')
            else:
                print('Opção inválida\n'
                      'Tente novamente!\n'
                      'use as opções do menu\n')

            P = input('Quer saber mais detalhes da rede?\n'
                      'S - sim\n'
                      'N - não\n'
                      '>> ')
    except:
        print('Opção inválida\n'
              'Tente novamente!\n'
              'Use as opções do menu\n')
        continue
    if P == 'N' or P == 'n':
        break
    else:
        print('Opção inválida\n'
              'Tente novamente!\n'
              'Use as opções do menu\n')
        continue
print('Fim do programa!')