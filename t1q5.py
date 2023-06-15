def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado
def mesExtenso(mes):
    if mes == 1:
        return 'JANEIRO'
    elif mes == 2:
        return "FEVEREIRO"
    elif mes == 3:
        return 'MARÇO'
    elif mes == 4:
        return 'ABRIL'
    elif mes == 5:
        return 'MAIO'
    elif mes == 6:
        return 'JUNHO'
    elif mes == 7:
        return 'JULHO'
    elif mes == 8:
        return 'AGOSTO'
    elif mes == 9:
        return 'SETEMBRO'
    elif mes == 10:
        return 'OUTRUBRO'
    elif mes == 11:
        return 'NOVEMBRO'
    elif mes == 12:
        return 'DEZEMBRO'

def desempacota(uf, ibge, nome, dia, mes, pop):
    return f'{nome}({uf}) tem {pop} habitantes e faz aniversário em {dia} de {mesExtenso(mes).lower()}.'

def populacao(pop, mes, cidades):
    saida = []
    for linha in cidades:
        if linha[5] >= pop and mes == linha[4]:
            saida.append(desempacota(*linha))
    return saida

def imprimeLista(lista):
    for linha in lista:
        print(linha)

def main():
    cidades = carrega_cidades()
    mes = int(input())
    pop = int(input())

    cidadesPopulacao = populacao(pop, mes, cidades)
    print(f"CIDADES COM MAIS DE {pop} HABITANTES E ANIVERSÁRIO EM {mesExtenso(mes)}:")
    imprimeLista(cidadesPopulacao)

if __name__ == '__main__':
    main()





