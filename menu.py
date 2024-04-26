import random
from jogadores import Jogadores, Ranking

desenhos_forca = [
    "  __\n |    |\n |\n |\n |\n |\n|",
    "  __\n |    |\n |    O\n |\n |\n |\n|",
    "  __\n |    |\n |    O\n |    |\n |\n |\n|",
    "  __\n |    |\n |    O\n |   /|\n |\n |\n|",
    "  __\n |    |\n |    O\n |   /|\\\n |\n |\n|",
    "  __\n |    |\n |    O\n |   /|\\\n |   /\n |\n|"
]

def choose_word1():
    with open("palavras1.txt", "r") as file:
        lines = file.readlines()
    word_info = random.choice(lines).strip().split(",")
    word = word_info[0].lower()
    hint = word_info[1].strip()
    return word, hint

def choose_word2():
    with open("palavras2.txt", "r") as file:
        lines = file.readlines()
    word_info = random.choice(lines).strip().split(",")
    word = word_info[0].lower()
    hint = word_info[1].strip()
    return word, hint

def choose_word3():
    with open("palavras3.txt", "r") as file:
        lines = file.readlines()
    word_info = random.choice(lines).strip().split(",")
    word = word_info[0].lower()
    hint = word_info[1].strip()
    return word, hint

def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    return display

def display_forca(erros):
    print(desenhos_forca[erros])

print('----------------------------------------------')
print('BEM VINDO AO JOGO DA FORCA')
print('----------------------------------------------')
print()

while True:
    nome = Jogadores(
        input('Digite seu nickname: '), 0, 0, 0)
    print()
    if not nome.cheka_nickname():
        nome.salva_nickname()

    print()
    
    ranking = Ranking(None, None, None, None)
    ranking.ranking()


    print()

    nome.mostrar_info()

    print()
    opc = input('Começar jogo? (s:sim, n:não): ')

    if opc == 's':
        dificuldade = input('Escolha a dificuldade: fácil(1), difícil(2), IMPOSSIVEL(3): ')
        if dificuldade == '1':
            print('Jogo na dificuldade 1')
            pontos_de_vitoria = 500
            word = choose_word1()
        elif dificuldade == '2':
            pontos_de_vitoria = 1000
            print('Jogo na dificuldade 2')
            word = choose_word2()
        elif dificuldade == '3':
            pontos_de_vitoria = 2000
            print('Jogo na dificuldade 3')
            word = choose_word3()
        else:
            print('Digite uma dificuldade válida.')

        print('Começar jogo...')

        if dificuldade == '1':
            print('Jogo na dificuldade 1')
            print('')
            pontos_de_vitoria = 500
            word, hint = choose_word1()
            print("Dica:", hint)
        elif dificuldade == '2':
            pontos_de_vitoria = 1000
            print('Jogo na dificuldade 2')
            print('')
            word, hint = choose_word2()
            print("Dica:", hint)
        elif dificuldade == '3':
            pontos_de_vitoria = 2000
            print('Jogo na dificuldade 3')
            print('')
            word, hint = choose_word3()
            print("Dica:", hint)
        
        guessed_letters = []
        attempts = 6
        diminuidor_pontos = 0
        while attempts > 0:

            print("\nPalavra: ", display_word(word, guessed_letters))
            display_forca(6 - attempts)
            guess = input("Digite uma letra: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Por favor, insira apenas uma letra válida.")
                continue

            if guess in guessed_letters:
                print("Você já tentou esta letra. Tente outra.")
                continue

            guessed_letters.append(guess)

            if guess not in word:
                attempts -= 1
                print("Letra incorreta! Você tem {} tentativas restantes.".format(attempts))
                diminuidor_pontos += 100
            else:
                print("Letra correta!")

            if "_" not in display_word(word, guessed_letters):
                print("\nParabéns! Você adivinhou a palavra: ", word)
                vitorias = 1
                while True:
                    opcao = input('DESEJA SALVAR O JOGO? (s:sim/n:não)')
                    if opcao == 's':
                        pontos_de_vitoria = pontos_de_vitoria - diminuidor_pontos
                        nome.atualiza(pontos_de_vitoria, vitorias, 0)
                        break
                    elif opcao == 'n':
                        print('jogo não foi salvo')
                        break
                    else:
                        print('digite corretamente')
                        continue
                break

            if attempts == 0:
                print("\nVocê perdeu! A palavra era: ", word)
                derrotas = 1
                while True:
                    opcao = input('DESEJA SALVAR O JOGO? (s:sim/n:não)')
                    if opcao == 's':
                        nome.atualiza(0, 0, derrotas)
                        break
                    elif opcao == 'n':
                        print('jogo não foi salvo')
                        break
                    else:
                        print('digite corretamente')
                        continue
                break
        continue

    elif opc == 'n':
        print('Jogo encerrado.')
        break

    else:
        print('Digite uma opção válida.')
        continue