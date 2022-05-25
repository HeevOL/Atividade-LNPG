def separador(arquivo:str):
    palavras = []
    caracteres = '. ( ) , ! @ # % * - + = / \ | [ ] { } ? : ;'.split()

    for linhas in arquivo:
        for caracter in caracteres:   
            linhas = linhas.replace(caracter, ' ')                
        palavras.extend(str(linhas).split())

    return palavras


def qntdPalavras(palavras):
    return len(palavras)


def palavrasMaiores(palavras):
    listaDePalavras = ['']
    for palavra in palavras:
        if len(palavra) > len(listaDePalavras[0]):
            listaDePalavras.clear()
            listaDePalavras.append(palavra)
        elif len(palavra) == len(listaDePalavras[0]):
            listaDePalavras.append(palavra)

    return listaDePalavras


def vogal(caminho):
    arquivo = open(caminho, "r", encoding="UTF-8")
    dic = {"a":0, "e":0, "i":0, "o":0, "u":0}
    for linha in arquivo:
        dic["a"] = dic["a"] + linha.lower().count('a')
        dic["e"] = dic["e"] + linha.lower().count('e')
        dic["i"] = dic["i"] + linha.lower().count('i')
        dic["o"] = dic["o"] + linha.lower().count('o')
        dic["u"] = dic["u"] + linha.lower().count('u')
    arquivo.close()   

    return max(dic, key=dic.get)


def literal(caminho):
    arquivo = open(caminho, "r", encoding="UTF-8")
    c = 1
    for linha in arquivo:
        if "ção" in linha:
            return c
            break
        else:
            c += 1 

    arquivo.close()


def main():
    caminho = input()
    arquivo = open(caminho, "r", encoding="UTF-8")
    palavrasArquivo = separador(arquivo)
    arquivo.close()
    print(f"Total de palavras: {qntdPalavras(palavrasArquivo)}")
    print(f"Maior(es) Palavra(s): {str(palavrasMaiores(palavrasArquivo))[1:-1]}")
    print(f"Vogal mais comum no arquivo: {vogal(caminho)}")
    print(f'Primeira aparição de "ção" é na linha: {literal(caminho)}')

main()