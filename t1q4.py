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

def desempacota(uf, ibge, nome, dia, mes, pop):
    return f'IBGE: {ibge} - {nome}({uf}) - POPULAÇÃO: {pop}'

def populacao(pop, cidades):
    saida = []
    for linha in cidades:
        if linha[5] >= pop:
            saida.append(desempacota(*linha))
    return saida

def imprimeLista(lista):
    for linha in lista:
        print(linha)

def main():
    cidades = carrega_cidades()
    pop = int(input())

    cidadesPopulacao = populacao(pop,cidades)
    print(f"CIDADES COM MAIS DE {pop} HABITANTES:")
    imprimeLista(cidadesPopulacao)

if __name__ == '__main__':
    main()





