menu = """
Digite uma Opção:
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

> Digite sua opção : """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES =3

while True:
        opção = input(menu).upper()

        if opção == 'D':
                valor = input('Informe o valor do deposito: ')
                valor = float(valor)

                if valor > 0:
                    saldo = valor
                    extrato == f'Depósito: R$ {valor}\n"'
                else:
                    print('Operação falhou! O valor informado é inválido.')

        elif opção =='S':
                valor_saque = input('Digite o valor do saque: ')
                valor_saque =  float(valor_saque)

                if valor_saque > saldo:
                    print('Operação falhou! Voce não possui saldo suficiente.')

                elif valor_saque > limite:
                    print('Operação falhou. O valor do saque excede o limite.')
                elif numero_saques >=LIMITE_SAQUES:
                    print('Operação falhou! Número de saques diários excedidos.')

                elif valor_saque >0:
                    saldo = saldo - valor_saque
                    extrato = (f'Saque: R${valor_saque}')
                    numero_saques +=1
                else:
                       print('Operação falhou! O valor informado é inválido. ') 

        elif opção =='E':
               print('\n ##### EXTRATO #####')
               print('Não foram realizadas movimentações financeiras.' if not extrato else extrato)
               print(f'Saldo R${saldo}')
               print('########')

        elif opção =='Q':
               break
        else:
            print('Operação inválida, por favor selecione novamente a opção desejada.')                   