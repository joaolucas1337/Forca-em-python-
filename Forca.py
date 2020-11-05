#Aluno: João Lucas De Souza Soares
#RA: N622DH-8
#Turma: CC2A30

import random

while True:
    print("\nBEM VINDO AO JOGO DA FORCA!\n")
    print("Para jogar, escolha as opções abaixo\n")
    opcoes = str(input("Para gravar palavras no jogo digite [G], para jogar digite [J], e para sair digite [S]: ")).upper() 

    if opcoes == 'G':
        nome_arquivo = "C:/Users/COMPUTADOR/Desktop/Programação Estruturada/palavras_forca.txt"
        arquivo = open(nome_arquivo, "w")
        
        palavras_add = []

        while True:
            palavras_para_add = True
            print('\n', palavras_add)
            palavra = str(input("\nDigite uma palavra pra ser usada na forca: "))
            if palavra in palavras_add:
                palavras_para_add = False
            else:
                palavras_add.append(palavra)
                arquivo.write(palavra + '\n')
            if palavras_para_add == False:
                print('\nVocê ja gravou esta palavra!')
            final = str(input('\nDeseja escrever outra palavra (S/N)?: ')).upper()
            if final != 'S':
                print('\nAs suas palavras foram adicionadas, agora continue jogando!')
                break
            
    
    if opcoes == 'J':
        nome_arquivo = "C:/Users/COMPUTADOR/Desktop/Programação Estruturada/palavras_forca.txt"
        arquivo = open(nome_arquivo, "r")
        palavras = arquivo.readlines()
        palavra_escolhida = random.choice(palavras)
        for palavra in palavra_escolhida:
            palavra = palavra_escolhida.rstrip('\n')

        tentativas = []
        acertos = []
        erros = 0

        while True:
            senha = ""
            for letras_acertadas in palavra:
                senha += letras_acertadas if letras_acertadas in acertos else ("'_'")
            print('\n' + senha)
            if senha == palavra:
                print('\nParabéns, você acertou a palavra!\n')
                novamente = input("Você deseja jogar novamente [S/N]: ").upper()
                if novamente == 'S':
                    break
                else:
                    print('\nAdeus!')
                    exit(0)
            chute = input('\nDigite uma letra: ').lower()
            if chute in tentativas:
                print('\nVocê já usou essa letra !')
                continue
            else:
                tentativas += chute
                if chute in palavra:
                    acertos += tentativas
                else:
                    erros += 1
                    print("\nVocê errou, te restam {} tentativas!\n".format(4 - erros))
                    if erros == 4:
                        print("Você perdeu!")
                        novamente = input("\nVocê deseja jogar novamente [S/N]: ").upper()
                        if novamente == 'S':
                            break
                        else:
                            print('\nAdeus!')
                            exit(0)

    if opcoes == 'S':
        print('\nObrigado por jogar, adeus!')
        break