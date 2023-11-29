import functions

while True:
    menu = int(input('---------- BEM-VINDO AO MENU DE OPÇÕES ----------\n'         # Menu principal. menu -- variável criada para receber o input do menu principal.
                     '1 - Descrição da solução\n'
                     '2 - Questionário de saúde\n'
                     '3 - Calculadora de IMC (Índice de massa corporal)\n'
                     '4 - Cadastrar-se/Login\n'
                     '0 - SAIR\n'
                     'Selecione sua opção (0 a 4): '))

    match menu:
        case 1:                                                     # Descrição da solução (sobre o quiz de saúde).
            print('---------- DESCRIÇÃO DA SOLUÇÃO ----------\n'
                  '     Essa é a descrição da solução com objetivo de automatizar e acelerar os processos de atendimentos em clínicos gerais ou emergências.\n'
                  '     A saúde é uma área onde a inovação e a tecnologia estão desempenhando um papel vital. Com a'
                  'crescente conscientização sobre a importância da mesma,\n'
                  'soluções baseadas em dados, wearables e aplicativos estão capacitando as pessoas a monitorá-la de forma'
                  'mais eficaz e promovendo o Home & Personal Care.\n'
                  'Essas tecnologias não apenas melhoram a eficiência dos procedimentos médicos, mas também reduzem os riscos e a margem de erro, proporcionando resultados mais consistentes e confiáveis.\n'
                  '     Nossa solução consiste em desenvolver um "questionário", atualizado a cada três (3) meses,\n'
                  'que sirva como triagem/anamnese de pacientes que buscam assistência médica em clínicos gerais, ou até mesmo sejam levados à unidade de emergência.\n'
                  'Esse questionário contém perguntas básicas sobre a saúde do paciente, como: "Você pratica algum esporte?", "Usa alguma droga, fuma, bebe?", "Teve alguma doença recentemente? Qual?".\n'
                  'São perguntas simples, porém, capazes de adiantar o processo inicial de atendimento do paciente, reduzindo o tempo de espera e as filas nos postos de saúde.\n'
                  'Em casos emergenciais, o questionário também conterá informações como tipo sanguíneo, alergia a medicamentos, problemas cardíacos, cirurgias anteriores.\n'
                  'A ideia é manter essas informações com fácil acesso, porém somente por pessoas habilitadas. O tempo ganho com a ausência da demora ao acesso a essas informações pode salvar uma vida.')

        case 2:  # IMPLEMENTAÇÃO DO QUESTIONÁRIO EM FORMA DE FUNÇÃO (executar_quiz()).
            functions.executar_quiz()

        case 3:  # IMPLEMENTAÇÃO DA CALCULADORA DE IMC EM FORMA DE FUNÇÃO (calcular_imc(altura, peso)).
            print('---------- CALCULADORA DE IMC ----------\n'
                  'Vamos agora calcular seu IMC, sigua as instruções na tela.\n')

            while True:       # Estrutura de repetição que permite uma nova chance de input caso o usuário insira caracteres não permitidos.
                try:
                    peso = float(input('Informe seu peso (em quilogramas, ex: 80): '))
                    altura = float(input('Informe sua altura (em metros, ex: 1.95): '))

                    imc = functions.calcular_imc(altura, peso)  # Função que recebe os parâmetros "altura" e "peso" e retorna o resultado do IMC.

                    print(f'Seu IMC é de: {imc:.2f}')

                    if imc < 17:
                        print('Você está muito abaixo do peso.')
                    elif 17 <= imc < 18.5:
                        print('Você está razoavelmente abaixo do peso.')
                    elif 18.5 <= imc < 25:
                        print('Você está com o peso normal.')
                    elif 25 <= imc < 30:
                        print('Você está acima do peso.')
                    elif 30 <= imc < 35:
                        print('Você está com obesidade de grau 1.')
                    elif 35 <= imc <= 40:
                        print('Você está com obesidade de grau 2.')
                    else:
                        print('Você está com obesidade de grau 3.')

                    break

                except ValueError:       # Tratamento de erro pra caso o usuário insira algum caracter de texto nas variáveis float.
                    print('Os valores devem ser compostos apenas por números.')


        case 4: # MENU DE CADASTRO
            while True:
                cad_log = int(input('---------- CADASTRAR-SE/LOGIN ----------\n'     # cad_log -- variável criada para receber o input do menu.
                                    '1 - Cadastrar-se\n'
                                    '2 - Login\n'
                                    '0 - VOLTAR\n'
                                    'Selecione uma opção (0 a 2): '))

                match cad_log:
                    case 1:
                        functions.realizar_cadastro()  # Função responsável por cadastrar o paciente no sistema, armazenando suas informações em variáveis globais.
                        break

                    case 2:
                        functions.realizar_login()     # Função responsável por realizar o Login do paciente no sistema, utilizando as informações previamente cadastradas.
                        break
                    case 0:       # Volta pro menu principal.
                        break
                    case _:
                        print('Opção inválida, tente novamente.')

        case 0: # Finalizador do menu
            print('Menu finalizado.')
            break
        case _:
            print('Opção inválida. Selecione entre 0 e 4.')  # Executado caso o usuário insira algum input fora das opções de 0 a 4 no menu principal.