print('='*50)
print('BOTS by VtMIGUEL \n"Bots a seu alcance!"')
print('='*50)

atendimento = int(input('[1] - Whatsapp \n[2] - OUTROS \nDigite a modalidade do seu Bot: '))
presencial = 1
if atendimento == 1:
    print('Agora você precisa informar os dados abaixo')
    cidade = input('Digite a cidade: ')
    bairro = input('Bairro: ')
    num = int(input('Número: '))
    ponto = input('Ponto de referência: ')
    fora = input('É fora do RJ? \n[A] - Sim \n[B] - Não \n[]: ')
    a = 'sim'
    b = 'não'
    if fora == a:
        print('Ok! Vamos continuar!!!')
    else:
        print('Terá custos adicionais conforme a localidade')
else:
    programa = str(input('Digite para qual site ou programa deseja seu Bot: '))
    finalidade = input('Qual a finalidade do Bot?: ')
    quantidade = input('Quantos usuários: ')
    tempo = input('Em quanto tempo quer o Bot?: ')

    confirma = int(input('Você marcou às {} horas, na {}. \nNo estado de {} na cidade de {}. \nTe esperamos na {}!'
                         ''.format(programa, finalidade, quantidade, tempo)))