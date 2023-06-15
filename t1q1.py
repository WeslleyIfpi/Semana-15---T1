def main():
    temperaturaA = (float(input()), input().upper()[0])
    temperaturaB = (float(input()), input().upper()[0])

    if temperaturaA[1] == temperaturaB[1]:
        maisAlta = temperaturaA if temperaturaA[0] > temperaturaB[0] else temperaturaB 
    else:
        if temperaturaA[1] == 'F':
            converte = (temperaturaA[0]- 32) / 1.8
            maisAlta = temperaturaB if temperaturaB[0]> converte else temperaturaA
        else:
            converte = (temperaturaB[0]- 32) / 1.8
            maisAlta = temperaturaA if temperaturaA[0]> converte else temperaturaB
    
    print(maisAlta)

if __name__ == '__main__':
    main()