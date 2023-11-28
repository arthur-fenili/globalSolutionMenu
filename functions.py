def calcular_imc(altura, peso):

    imc = peso / altura ** 2

    return imc

def executar_quiz(): #################

    global lista_remedios, profissao, pratica_esporte, doenca_seria, usuario, pressao_alta, diabetes

    lista_remedios = []

    print('---------- QUESTIONÁRIO DE SAÚDE ----------\n'
          'Esse é o questionário responsável por armazenar suas informações de saúde e agilizar os processos de triagem.\n'
          'Você respoderá algumas breves perguntas, aquelas mesmas de sempre, só que desta vez as respostas ficarão armazenadas no banco de dados.\n'
          'Não se preocupe, ninguém, a não ser o médico, terá acesso a essas informações. Desta forma, seus atendimentos se tornarão mais ágeis, e sua assistência médica estará disponivel mais rápido!\n')

    while True:
        start_quiz = int(input('Gostaria de começar? 1 - Sim / 2 - Não\n'
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