# -*- coding: utf-8 -*-
#Projeto Super
#Task: WP3-CETELI-2-IA
#Curso: Programação Python
#Bolsista 1: Alex Rocha
#Bolsista 2: Diego Vieira
#Bolsista 3: Thayla Moura

import random

def criarBase(nome):
    #essa lista define as palavras do jogo
    palavras = "banana acerola caju laranja verde vermelho azul rosa carro moto barco casa cidade aula viajem pai comida aviao gato pizza escola"
    #esse bloco criar um arquivo nome.txt escreve a string palavras
    base = open(nome, 'w')
    base.write(palavras)
    base.close()

#essa função recupera as palavras do arquivo nome.txt em uma variável palavras
def listarPalavras(nome):
    base = open(nome, 'r')
    palavras = base.read().split()
    base.close()
    return palavras

#essa função cria os parâmetros do jogo
def criarJogo():
    nome = "base.txt"
    criarBase(nome)
    palavra = random.choice(listarPalavras(nome))
    montagem = []
    for n in range(len(palavra)):
        montagem.append("-")
    jogo = dict(palavra = palavra, montagem = montagem, acertos = [], erros = [], quantPalpites = 0, terminou = False, ganhou = False)
    return jogo

#essa função pega os dados do jogador da partida
def criarJogador():

    nome = str(input("Insira seu nome: "))
    email = str(input("Insira seu email: "))
    jogador = dict(nome = nome, email = email)
    print("")
    return jogador

#essa funlão valida a entrada do usuário em termos de palpites no jogo
def validarEntrada(letra, acertos):
    if(len(letra) > 1):
        print("Insira apenas uma letra!")
        return False
    elif(not letra.isalpha()):
        print("Insira uma letra do alfabeto!")
        return False
    elif(letra in acertos):
        print("Insira uma letra diferente!")
        return False
    else: return True

#essa função permite ao jogador fazer uma jogada
def fazerJogada(jogo):
    if(len(jogo['erros']) <= 5):
        letra = str(input("\nInsira uma letra: ").lower())
        if(not validarEntrada(letra, jogo['acertos'])):
            fazerJogada(jogo)
        elif(letra not in jogo['palavra']):
            jogo['erros'].append(letra)
            print("A letra inserida não ocorre na palavra.\n")
        else:
            jogo['acertos'].append(letra)
            print("Você acertou uma letra!\n")
            for n in range(len(jogo['palavra'])):
                if(jogo['palavra'][n] == letra): jogo['montagem'][n] = letra
            if(jogo['palavra'] == "".join(jogo['montagem'])):
                print("Parabéns, você acertou todas as letras da palavra e terminou o jogo!\n")
                jogo['terminou'] = jogo['ganhou'] = True
    else:
        print("Você já usou todas sua tentativas.\n")
        jogo['terminou'] = True

#essa função permite ao jogador fazer um palpite
def fazerPalpite(jogo):
    if(jogo['quantPalpites'] <= 3):
        palpite = str(input("\nInsira seu palpite: ").lower())
        if(palpite == jogo['palavra']):
            print("Parabéns, você acertou a palavra e terminou o jogo!\n")
            jogo['terminou'] = jogo['ganhou'] = True
        else:
            jogo['quantPalpites'] += 1
            print("Palpite incorreto.")
    else:
        print("Você já usou todos seus palpites.\n")
        jogo['terminou'] = True

#essa função mostra o resumo da partida
def imprimirResumo(jogo):
    print("Palavra: ", end = "")
    for letra in jogo['montagem']:
        if(letra == '-'): print("_ ", end = "")
        else: print("%s " % letra, end = "")
    print("\n\nLetras acertadas: ", jogo['acertos'])
    print("Letras erradas: ", jogo['erros'])
    print("Tentativas de letra disponíveis: ", 5 - len(jogo['erros']))
    print("Palpites disponíveis: ", 3 - jogo['quantPalpites'])

#essa função salva o resultado do jogo num arquivo
def salvarJogo(jogo, jogador):
    arquivo = open("jogo.txt", 'a')
    arquivo.write(jogador['nome'] + "\n")
    arquivo.write(jogador['email'] + "\n")
    arquivo.write(jogo['palavra'] + "\n")
    arquivo.write("Ganhou: " + str(jogo['ganhou']) + "\n\n")
    arquivo.close()

#essa é a função principal do jogo da forca
def main():
    jogo = criarJogo()
    print("Bem-vindo ao jogo de forca em Python!\n")
    jogador = criarJogador()
    imprimirResumo(jogo)
    fazerJogada(jogo)
    imprimirResumo(jogo)

    while(not jogo['terminou']):
        res = str(input("\nGostaria de tentar mais uma letra ou tentar um palpite da palavra? (L/P): ").upper())
        if(res == 'L'):
            fazerJogada(jogo)
            imprimirResumo(jogo)
        elif(res == 'P'): fazerPalpite(jogo)
        else: print("Opção inválida!")
    salvarJogo(jogo, jogador)

main()