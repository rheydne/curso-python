
def operation(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/' and number2 == 0:
        print('Operação Inválida!!!')
    elif operator == '/':
        return number1 / number2
    else:
        print('Operação Inválida!!!')


print('========>> Calculator <<========')

number1 = float(input('Insira um número: '))
operator = str(input('Insira o operador matemático (+ - * /): '))
number2 = float(input('Insira outro número: '))

result = operation(number1, number2, operator)

print(f'O resultado da operaçao {number1} {operator} {number2} = {result}')
