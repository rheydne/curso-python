import random


def EscolhePalavra():

    palavras = ['uva', 'banana', 'pera']

    palavra_escolhida = random.randint(0, len(palavras) - 1)
    palavra_escolhida = palavras[palavra_escolhida]

    return palavra_escolhida


def EscondePalavra(palavra_escolhida): 

    (palavra_escondida) = ''

    for i in palavra_escolhida:
        (palavra_escondida) += '_ '

    return((palavra_escondida))


def VerificaLetraDigitada(letras_digitadas, palavra_escolhida):

    resultado_parcial = ''  
    for letra in palavra_escolhida:
        if letra in letras_digitadas:
            resultado_parcial += letra + ' '
        else:
            resultado_parcial += '_ '

    return resultado_parcial


def PossuiLetraNaPalavra(letra, palavra_escolhida):
    validacao = 1
    for i in palavra_escolhida.strip():
        if letra == i:
            validacao = 0

    return validacao


cont = 0
erros_permitidos = 6
letras_digitadas = ''
erros_realizados = 0

palavra_escolhida = EscolhePalavra()
palavra_escondida = EscondePalavra(palavra_escolhida)

while erros_realizados < erros_permitidos:

    print('------------------------------------\n')
    print('J O G O  D A  F O R C A\n')
    print('Letras já digitadas: ')
    print(letras_digitadas)
    print('\nTente adivinhar a palavra sortida abaixo:')
    print(palavra_escondida)
    letra = input('\n\nDigite uma letra: ').strip()

    letras_digitadas += letra

    erros_realizados += PossuiLetraNaPalavra(letra, palavra_escolhida)
    palavra_escondida = VerificaLetraDigitada(letras_digitadas, palavra_escolhida)
    
    if erros_realizados == erros_permitidos:
        print('VOCE PERDEU!!!!!')
        break

    teste = 0
    for letra in palavra_escondida:
        if letra == '_':
            teste += 1

    if teste > 0:
        continue
    else:
        print('Você GANHOU!')
        print(palavra_escondida)
        break
    
