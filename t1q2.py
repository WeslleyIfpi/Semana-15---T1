def main():
    tuplaA = (float(input()), input().upper()[0])
    tuplaB = (float(input()), input().upper()[0])

    if tuplaA[1] == tuplaB[1]:
        soma = tuplaA[0] + tuplaB[0]
        tuplaC = (round(soma, 4), tuplaB[1])
    else:
        if tuplaB[1] == 'F':
            soma = (tuplaA[0] * 1.8 + 32) + tuplaB[0]
            tuplaC = (round(soma, 4), tuplaB[1])
        else:
            soma = ((tuplaA[0] - 32) / 1.8) + tuplaB[0]
            tuplaC = (round(soma, 4), tuplaB[1])
        
    print(tuplaC)



if __name__ == '__main__':
    main()