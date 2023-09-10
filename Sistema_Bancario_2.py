
#FUNÇÕES PAR OTIMIZAR SISTEMA BANCÁRIO

def exibir_menu():
    menu = ('''
      ========= MENU =========
           [1] SAQUE
           [2] DEPÓSITO
           [3] EXTRATO
           [4] CRIAR USUÁRIO
           [0] SAIR
      ========================\n---> ''')  # MENU DE OPÇÕES DO SISTEMA
    return input(menu)


def sacar(*, saldo, saque, extrato, numero_saque_diario, limite_saque_diario, limite_valor_saque):

    excedeu_saldo = saque > saldo
    excedeu_valor_saque = saque > limite_valor_saque
    excedeu_saque_diario = numero_saque_diario >= limite_saque_diario
    
    if excedeu_saldo:
        print('======================================')
        print('*OPERAÇÃO FALHOU* SALDO INSUFICIENTE')
    
    elif excedeu_valor_saque:
        print('======================================')
        print('*OPERAÇÃO FALHOU* EXCEDEU VALOR DE SAQUE')
    
    elif excedeu_saque_diario:
        print('======================================')
        print('*OPERAÇÃO FALHOU* LIMITE DE SAQUES DIÁRIO EXCEDEU')
    
    elif saque > 0:
        saldo -= saque
        numero_saque_diario += 1
        extrato += f'SAQUE DE R$ -{saque:.2f}\n'
        print('======================================')
        print('   [SAQUE REALIZADO COM SUCESSO]')
    
    else:
        print('======================================')
        print('*OPERAÇÃO FALHOU* VALOR INVÁLIDO')

    return saldo, extrato, numero_saque_diario
        

def depositar(saldo, deposito, extrato,/):

    if deposito > 0:
        saldo += deposito
        extrato += f'DEPÓSITO DE R$ +{deposito:.2f}\n'
        print('======================================')
        print('  [DEPÓSITO REALIZADO COM SUCESSO]')

    else:
        print('======================================')
        print('*OPERAÇÃO FALHOOU* VALOR INVÁLIDO')

    return saldo, extrato


def exibir_extrato(*, saldo, extrato):

    print('==============EXTRATO=============')
    print('NÃO HOUVE MOVIMENTAÇÕES NA CONTA !!\n' if not extrato else extrato)
    print(f'SALDO ATUAL R$ {saldo:.2f}')
    print('==================================')


def cadastrar_usuario(lista_usuarios):

    CPF = int(input('INFORME SEU CPF (SOMENTE NÚMEROS) -> ').strip())

    usuario_verificado = []
    # VERIFICAR SE O USUARIO JÁ ESTÁ CADASTRADO
    for usuario in lista_usuarios:
        usuario_verificado.append(usuario['CPF'])

    if CPF in usuario_verificado:
        print('======================================')
        print('  *FALHA* USUÁRIO JÁ ESTÁ CADASTRADO')
        return

    NOME = input('INFORME SEU NOME COMPLETO -> ')
    LOGRADOURO_NUMERO = input('INFORME SEU LOGRADOURO - NÚMERO -> ')
    BAIRRO = input('INFORME SEU BAIRRO -> ')
    CIDADE = input('INFORME SUA CIDADE -> ')
    ESTADO_SIGLA = input('INFORME A SIGLA DO ESTADO -> ')
    print('======================================')
    print('   USUÁRIO CADASTRADO COM SUCESSO')

    lista_usuarios.append({'CPF': CPF, 'nome': NOME, 'logradouro': LOGRADOURO_NUMERO, 
                           'bairro': BAIRRO, 'cidade': CIDADE, 'estado': ESTADO_SIGLA})

    return lista_usuarios


def main():
    LIMITE_SAQUE_DIARIO = 3
    LIMITE_VALOR_SAQUE = 500
    
    saldo = 0
    numero_saque_diario = 0
    extrato = ''
    lista_usuarios = []
   
    while True:
        
        opcao = exibir_menu()
        
        if int(opcao) == 1:  # SAQUE

            saque = float(input('INFORME O VALOR PARA SAQUE -> R$ ')) 

            saldo, extrato, numero_saque_diario = sacar(
                saldo=saldo,
                saque=saque,
                extrato=extrato,
                numero_saque_diario=numero_saque_diario,
                limite_saque_diario=LIMITE_SAQUE_DIARIO,
                limite_valor_saque=LIMITE_VALOR_SAQUE,
            )

        elif int(opcao) == 2:  # DEPÓSITO
            
            deposito = float(input('INFORME O VALOR DE DEPÓSITO -> R$ '))

            saldo, extrato = depositar(saldo, deposito, extrato)

        elif int(opcao) == 3:  # EXTRATO MAIS SALDO ATUAL DA CONTA

            exibir_extrato(saldo=saldo, extrato=extrato)

        elif int(opcao) == 4:  # CRIANDO UM USUARIO

            cadastrar_usuario(lista_usuarios)

        elif int(opcao) == 0:  # SAINDO DO MENU E ENCERRANDO A OPERAÇÃO

            print('======================================')
            print('[FIM DA OPERAÇÃO - TENHA UM ÓTIMO DIA]\n')
            break

        else:  # ITEM INFORMADO INCORRETO NO MENU

            print('======================================')
            print('*FALHA* OPÇÃO INVÁLIDA')

                  
main()





























