
# Exercicios em Python (uso de funcoes, strings e docstrings)
# Exercicio 1
# contar o numero de ocorrencias de um caracter numa string
# com exemplo de docstring


def contaOcorrencias(string, c):
    '''
        Retorna o numero de ocorrencias de um caracter numa string.
        (string, char) -> int
        >>> contaOcorrencias( "palavra", 'a' )
        3
        >>> contaOcorrencias( "palavra", 'e' )
        0
    '''
    contador = 0
    for a in string:
        if a == c:
            contador += 1
    return contador

# Exercicio 2
def primeiraPosicao(string, c):
    '''
        Retorna a primeira posição onde ocorre um caractere numa string.
        (string, char) -> int
        >>> primeiraPosicao("palavra", 'a')
        1
        >>> primeiraPosicao("palavra", 'e')
        -1
    '''
    return string.find(c)


#Exercicio 3
def contarEspacos(string):
    '''
        Retorna o número de espaços existentes numa string.
        (string) -> int
        >>> contarEspacos("a b c")
        2
        >>> contarEspacos("abc")
        0
    '''
    return string.count(' ')

#Exercicio 4
def removerEspacos(string):
    '''
        Retorna a string sem os espaços.
        (string) -> string
        >>> removerEspacos("a b c")
        'abc'
        >>> removerEspacos("   abc   ")
        'abc'
    '''
    return string.replace(' ', '')

#Exercicio 5
def removerNaoAlfabeticos(string):
    '''
        Retorna a string sem caracteres não alfabéticos.
        (string) -> string
        >>> removerNaoAlfabeticos("a1b2c!")
        'abc'
        >>> removerNaoAlfabeticos("123!!")
        ''
    '''
    return ''.join(filter(str.isalpha, string))

# Exercico 6
def caracteresOrdemPar(string):
    '''
        Retorna uma string apenas com os caracteres de índice par.
        (string) -> string
        >>> caracteresOrdemPar("abcdef")
        'ace'
        >>> caracteresOrdemPar("123456")
        '135'
    '''
    return string[::2]


# Exercicio 7
def substituirCaractere(string, antigo, novo):
    '''
        Substitui todas as ocorrências de um caractere por outro numa string.
        (string, char, char) -> string
        >>> substituirCaractere("banana", 'a', 'o')
        'bonono'
        >>> substituirCaractere("teste", 't', 'T')
        'TesTe'
    '''
    return string.replace(antigo, novo)

#Exercicio 8
def codigosAscii(string):
    '''
        Retorna uma lista com os códigos ASCII de cada caractere da string.
        (string) -> list[int]
        >>> codigosAscii("abc")
        [97, 98, 99]
        >>> codigosAscii("123")
        [49, 50, 51]
    '''
    return [ord(char) for char in string]


#Exercicio 9
def contarVogais(string):
    '''
        Retorna o número de vogais existentes numa string.
        (string) -> int
        >>> contarVogais("banana")
        3
        >>> contarVogais("xyz")
        0
    '''
    vogais = "aeiouAEIOU"
    return sum(1 for char in string if char in vogais)


#Exercicio 10

def verificarPalindromo(string):
    '''
        Retorna True se a string for um palíndromo, caso contrário False.
        (string) -> bool
        >>> verificarPalindromo("abccba")
        True
        >>> verificarPalindromo("teste")
        False
    '''
    string = string.lower().replace(" ", "")
    return string == string[::-1]

def main():
    s = input("Insira uma sequencia de caracteres: ")
    c = input("Insira o carácter a considerar: ")

    help(contaOcorrencias)

    o = contaOcorrencias(s, c)
    print("Ocorrencias de", c, "na string", '''"''', s, '''"''', ": ", o)
    print("\n-- Resultados --")
    print(f"Ocorrências de '{c}' em \"{s}\": {contaOcorrencias(s, c)}")
    print(f"Primeira posição de '{c}' em \"{s}\": {primeiraPosicao(s, c)}")
    print(f"Número de espaços em \"{s}\": {contarEspacos(s)}")
    print(f"String sem espaços: \"{removerEspacos(s)}\"")
    print(f"String sem caracteres não alfabéticos: \"{removerNaoAlfabeticos(s)}\"")


# testa se o modulo foi importado
# ou se esta a ser executado como programa principal
# (experimentar chamar a funcao main sem a instrucao if anterior)
if __name__ == '__main__':
    main()


