def calcular_imc(altura, peso):

    imc = peso / altura ** 2

    return imc

def executar_quiz():    # Função responsável por executar o questionário.

    global lista_remedios, profissao, pratica_esporte, doenca_seria, usuario, pressao_alta, diabetes

    lista_remedios = []

    print('---------- QUESTIONÁRIO DE SAÚDE ----------\n'
          'Esse é o questionário responsável por armazenar suas informações de saúde e agilizar os processos de triagem.\n'
          'Você respoderá algumas breves perguntas, aquelas mesmas de sempre, só que desta vez as respostas ficarão armazenadas no banco de dados.\n'
          'Não se preocupe, ninguém, a não ser o médico, terá acesso a essas informações. Desta forma, seus atendimentos se tornarão mais ágeis, e sua assistência médica estará disponivel mais rápido!\n')

    while True:
        start_quiz = int(input('Gostaria de começar? 1 - Sim / 2 - Não\n'      #start_quiz -- variável criada para receber o input do menu que começa o quiz.
                               'Resposta: '))

        if start_quiz == 1:

            profissao = input('Primeiro, informe sua profissão\n'
                              'Resposta: ')

            pratica_esporte = input('Você pratica algum esporte?\n'
                                    'Resposta (Sim/Não): ')
            print('Toma algum remédio? Se sim, responda com o nome do remédio. Caso seja mais de um, responda um por vez e aperte Enter. Quando terminar a lista, responda "n" ou "não" para finalizar.\n'
                  'Caso não tome nenhum remédio, responda "n" ou "não" para prosseguir.')
            while True:

                toma_remedio = input('Resposta: ')
                if toma_remedio == "Não" or toma_remedio == "não" or toma_remedio == "nao" or toma_remedio == "n" or toma_remedio == "N":
                    break
                else:
                    lista_remedios.append(toma_remedio)

            print(f'Sua lista de remédios = {lista_remedios}')

            doenca_seria = input('Teve alguma doença séria nos últimos anos?\n'
                                 'Resposta (Sim/Não): ')

            usuario = input('Você bebe, fuma ou usa alguma droga? Se sim, o que, e com que frequência?\n'
                            'Resposta (ex: Cerveja, 2x por semana): ')

            pressao_alta = input('Você possui pressão alta?\n'
                                 'Resposta (Sim/Não): ')

            diabetes = input('Sofre com diabetes?\n'
                             'Resposta (Sim/Não): ')

            print('Questionário finalizado. Suas informações foram salvas. Retornando ao menu principal.')
            break

        elif start_quiz == 2:
            print('Questionário cancelado. Retornando ao menu principal.')
            break

        else:
            print('Opção inválida. Tente novamente.') #####################

def realizar_cadastro():    # Função responsável por cadastrar o paciente no sistema, armazenando suas informações em variáveis globais.

    global nome_completo, email, senha, idade, cpf          # Variáveis globais podem ser acessadas ou verificadas por outras funções.

    print('Vamos realizar o seu cadastro no nosso sistema, siga as instruções na tela.\n'
          'Digite "SAIR" a qualquer momento para cancelar o cadastro.')
    while True:
        nome_completo = input('Primeiro, infome seu nome completo.\n'
                              'Resposta: ')

        if nome_completo == 'SAIR':
            print('Cadastro cancelado.')
            break

        cpf = input('Informe seu CPF (Ex: 123.321.999-00).\n'
                    'Resposta: ')

        if cpf == 'SAIR':
            print('Cadastro cancelado.')
            break

        email = input('Qual e-mail deseja cadastrar?\n'
                      'Resposta: ')

        if email == 'SAIR':
            print('Cadastro cancelado.')
            break

        senha = input('Por último, qual senha deseja cadastrar?\n'
                      'Resposta: ')

        if senha == 'SAIR':
            print('Cadastro cancelado.')
            break

        resposta_cad = int(input(f'Seu nome é {nome_completo}\n'        # resposta_cad -- variável que identifica o input do usuário e verifica se o cadastro está correto.
                                 f'CPF: {cpf}\n'
                                 f'E-mail: {email}\n'
                                 f'Senha: {senha}\n'
                                 'Confirma? 1 - Sim / 2 - Não (Esta opção realizará o cadastro novamente).\n'
                                 'Resposta: '))

        match resposta_cad:
            case 1:
                print('Cadastro realizado com sucesso!')
                break
            case 2:
                break

def realizar_login():   # Função responsável por realizar o Login do paciente no sistema, utilizando as informações previamente cadastradas.

    while True:

        if 'email' not in globals():                            # Identifica se a variável "email" foi preenchida (inicializada), isto é, se o usuário já realizou o cadastro.
            print('Você tem que realizar um cadastro primeiro.')
            break

        input_email = input('E-mail cadastrado: ')              # Variável criada para validação de informações. (e-mail)

        input_senha = input('Senha: ')                          # Variável criada para validação de informações. (senha)

        if input_email == email and input_senha == senha:
            print('Login realizado com sucesso!')
            break
        elif input_email != email:
            print('E-mail incorreto, tente novamente.')
        elif input_senha != senha:                                      # Caso o login esteja incorreto, essas mensagens aparecerão.
            print('Senha incorreta, tente novamente.')                  # Elas são personalizadas, ou seja, dependendo do que estiver errado, a mensagem muda.
        elif input_email != email and input_senha != senha:
            print('E-mail e senha incorretos, tente novamente.')
