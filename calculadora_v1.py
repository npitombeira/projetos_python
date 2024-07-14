operadores = ['+', '-', '*', '/', '**']

while True:
        numero_1 = input('Digite um número: ')
        validacao_numero_1 = numero_1.isdigit()        
        if validacao_numero_1:
            numero_1 = int(numero_1)
        else:
            while validacao_numero_1 is False:
                numero_1 = input(f'O valor informado "{numero_1}" não é um inteiro. Informe um número inteiro válido: ')
                validacao_numero_1 = numero_1.isdigit()
                
        numero_2 = input('Digite outro número: ')
        validacao_numero_2 = numero_2.isdigit()        
        if validacao_numero_2:
            numero_2 = int(numero_2)                
        else:
            while validacao_numero_2 is False:
                numero_2 = input(f'O valor informado "{numero_2}" não é um inteiro. Informe um número inteiro válido: ')
                validacao_numero_2 = numero_2.isdigit()
        
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)
                
        print('Qual operacao você deseja realizar? \n\n',
                        f'[{operadores[0]}] para SOMA\n',
                        f'[{operadores[1]}] para SUBTRAÇÃO\n',
                        f'[{operadores[2]}] para MULTIPLICAÇÃO\n',
                        f'[{operadores[3]}] para DIVISÃO\n',
                        f'[{operadores[4]}] para EXPONENCIAÇÃO\n')
        operacao = input('Informe APENAS um dos operadores listados acima: ')        
        validacao_operador = operacao in operadores
        
        while validacao_operador is False:
            operacao = input(f'Você forneceu o operador "{operacao}". Este operador é diferente das opções disponíveis. Informe um operador válido: ')        
            validacao_operador = operacao in operadores
        if operacao == '+':
            print(f'Você está realizando uma operação de SOMA: {numero_1} + {numero_2} = {numero_1 + numero_2}.')
        elif operacao == '-':
            print(f'Você está realizando uma operação de SUBTRAÇÃO: {numero_1} - {numero_2} = {numero_1 - numero_2}.')
        elif operacao == '*':
            print(f'Você está realizando uma operação de MULTIPLICAÇÃO: {numero_1} * {numero_2} = {numero_1 * numero_2}.')
        elif operacao == '/':
            print(f'Você está realizando uma operação de DIVISÃO: {numero_1} / {numero_2} = {numero_1 / numero_2}.')
        elif operacao == '**':
            print(f'Você está realizando uma operação de EXPONENCIAÇÃO: {numero_1} ** {numero_2} = {numero_1 ** numero_2}.')
        else:
            print(f'Você forneceu o operador "{operacao}". Este operador é diferente das opções disponíveis. Tente novamente informando um operador válido.')        
        sair = input('Quer sair? [s]im ').lower().startswith('s')
        if sair:
            print('Programa encerrado.')
            break