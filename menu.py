import functions

while True:
    menu = int(input('---------- BEM-VINDO AO MENU DE OPÇÕES ----------\n' # MENU PRINCIPAL 
                     '1 - Descrição da solução\n'
                     '2 - Quiz de saúde\n'
                     '3 - Cálculo de IMC (Índice de massa corporal)\n'
                     '4 - Cadastrar-se/Login\n'
                     '0 - SAIR\n'
                     'Selecione sua opção (0 a 4): '))

    match menu:
        case 1: # DESCRIÇÃO DA SOLUÇÃO (SOBRE O QUIZ DE SAÚDE)
            print('')
        case 2: # IMPLEMENTAÇÃO FUTURA DO QUIZ EM FORMA DE FUNÇÃO (executar_quiz())
            print('')
        case 3: # IMPLEMENTAÇÃO FUTURA DO CALCULO DE IMC EM FORMA DE FUNÇÃO (calcular_imc(altura, peso))
            print('')
        case 4: # MENU DE CADASTRO
            cad_log = int(input('---------- CADASTRAR-SE/LOGIN ----------\n'
                                '1 - Cadastrar-se\n'
                                '2 - Login\n'
                                '0 - VOLTAR\n'
                                'Selecione uma opção (0 a 2): '))

        case 0: # FINALIZADOR DO MENU
            print('Menu finalizado.')
            break