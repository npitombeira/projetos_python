lista_operadores = ['+', '-', '*', '/', '**']

def digite_um_numero(mensagem):
    while True:
            numero = input(mensagem)
            try:
                num_float= float(numero)
            except ValueError:
                print(f'Tipo inválido: O valor apresentado não é um número.')
                continue
            return float(numero)

def digite_uma_operacao():
        print('Qual operacao você deseja realizar? \n\n',
                        f'[{lista_operadores[0]}] para SOMA\n',
                        f'[{lista_operadores[1]}] para SUBTRAÇÃO\n',
                        f'[{lista_operadores[2]}] para MULTIPLICAÇÃO\n',
                        f'[{lista_operadores[3]}] para DIVISÃO\n',
                        f'[{lista_operadores[4]}] para EXPONENCIAÇÃO\n')
        operacao = input('Informe APENAS um dos operadores listados acima: ')
        validacao_operador = operacao in lista_operadores
        while not validacao_operador:
            operacao = input(f'Você forneceu o operador "{operacao}". Este operador é diferente das opções disponíveis. Informe um operador válido: ')        
            validacao_operador = operacao in lista_operadores
        return operacao

def calculadora(num1, num2, operador):
        if operador == '+':
            return num1 + num2
        elif operador == '-':
            return num1 - num2
        elif operador == '*':
            return num1 * num2
        elif operador == '/':
            try:
                return num1 / num2
            except ZeroDivisionError:
                print(f'Não foi possível executar a expressão "{num1} / {num2}", pois não é possível obter o resultadod e uma divisão por zero.')
                return  None
        elif operador == '**':
            print(f'Você está realizando uma operação de EXPONENCIAÇÃO: {num1} ** {num2} = {num1 ** num2}.')
            return num1 ** num2

while True:
    numero1 = digite_um_numero('Digite um número: ')
    numero2 = digite_um_numero('Digite outro número: ')
    operador = digite_uma_operacao()
    resultado = calculadora(num1=numero1, num2=numero2, operador=operador)
    
    if resultado is not None:
        print(f'O resultado de {numero1} {operador} {numero2} é {resultado}.')
    
    sair = input('Deseja encerrar o programa? [S]im ').lower().startswith('s')
    if sair:
        print('Programa encerrado.')
        break