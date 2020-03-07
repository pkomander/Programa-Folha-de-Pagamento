#dados do funcionario
def cadastrofuncionario(nome, numero_funcionario, ctps, cpf):
    print (f'Nome: {nome}')
    print (f'Numero de registro do funcionario: {numero_funcionario}')
    print (f'Numero da CTPS do funcionairo: {ctps} ')
    print (f'Numero do CPF do funcionario: {cpf}')



def salariodomes(hora_mes, dias_mes, salario_mes):
    print(f'O funcionario trabalhou {hora_mes} horas em {dias_mes} dias no mes o salario do funcionario e R${total_mes}')



def calculohoraextra(valor_hora, hora_extra, calculo_extra, acrescimo, total):
    print(f'Voce trabalhou {hora_extra} horas extra e o valor de uma hora e R$ {valor_hora} ')
    print(f'Voce deve receber de hora extra R$ {calculo_extra} mais um acrescimo de 50%  {acrescimo} totalizando R$ {total}')



def totalsalario(total_salrio_mes):
    print (f'O total do salario do mes do funcionario e de {total_salario_mes}')



def folhadepagamento(folha):
    print (folha)





#iniciar folha de pagamento
iniciar_folha= int(input('Voce deseja iniciar a folha de pagamento 1-SIM 2-NAO: '))
if iniciar_folha == 1:
    nome = input('Digite o nome do funcionario: ')
    numero_funcionario = int(input('Digite o numero de registro do funcionario: '))
    ctps = int(input('Digite o numero da CTPS do funcionario: '))
    cpf = int(input('Digite o numero do CPF do funcionario: '))
    cadastrofuncionario(nome, numero_funcionario, ctps, cpf)






    #calculo de horas trabalhadas no mes
    hora_mes= float(input('Digite a quantidade de horas trabalhadas no mes: '))
    dias_mes= int(input('Digite quantos dias foram trabalhados no mes: '))
    salario_mes= float(input('Digite o valor da hora trabalhada: '))
    if dias_mes <= 31:
        calculo_salario= hora_mes * salario_mes
        total_mes= calculo_salario * dias_mes
        salariodomes(hora_mes, dias_mes, salario_mes)
    else:
        print ('Os dias trabalhados estao fora do padrao de 31 dias!')







    # calculo da hora extra
    pergunta = int(input('Voce trabalhou hora extra 1-SIM 2-NAO: '))
    if pergunta == 1:
        valor_hora = float(input('Digite o valor de uma hora extra de trabalho: '))
        hora_extra = float(input('Digite a quantidade de horas extra: '))
        if hora_extra > 0:
            # calculo do valor da hora extra
            calculo_extra = valor_hora * hora_extra

            # calculo do acrecimo de 50%
            acrescimo = calculo_extra * 0.5

            # total
            total = calculo_extra + acrescimo
            #print('Voce trabalhou ', hora_extra, 'horas e o valor de uma hora e R$', valor_hora, '')
            #print('Voce deve receber de hora extra R$', calculo_extra, ' mais um acrescimo de 50% ', acrescimo, 'totalizando R$', total)
            calculohoraextra(valor_hora, hora_extra, calculo_extra, acrescimo, total)



            #total do salario do mes
            total_salario_mes= (total_mes + total)
            totalsalario(total_salario_mes)



            #folha de pagamento
            #objeto folha de pagamento
            #Em folha de pagamento tentei colocar a string print da mensagem feita apos o calculo da hora extra porem se repete e não possivel comentar a string na função para ser exibida somente no objeto.
            folha=[cadastrofuncionario(nome, numero_funcionario, ctps, cpf), salariodomes(hora_mes, dias_mes, salario_mes) , calculohoraextra(valor_hora, hora_extra, calculo_extra, acrescimo, total) , totalsalario(total_salario_mes)]

            folhadepagamento (folha)

    else:
        print('Voce nao trabalhou hora extra!')

else:
    print ('Voce nao iniciou a folha de pagamento!')



###########
#calculo da hora extra
#pergunta= int(input('Voce trabalhou hora extra 1-SIM 2-NAO: '))
#if pergunta == 1:
    #valor_hora= float(input('Digite o valor de uma hora de trabalho: '))
    #hora_extra= float(input('Digite a quantidade de horas extra: '))
    #if hora_extra > 0:
        #calculo do valor da hora extra
        #calculo_extra= valor_hora * hora_extra

        #calculo do acrecimo de 50%
        #acrescimo= calculo_extra * 0.5

        #total
        #total= calculo_extra + acrescimo
        #print ('Voce trabalhou ', hora_extra,'horas e o valor de uma hora e R$', valor_hora,'')
        #print ('Voce deve receber de hora extra R$', calculo_extra, ' mais um acrescimo de 50% ', acrescimo, 'totalizando R$', total)
#else:
    #print ('Voce nao trabalhou hora extra!')