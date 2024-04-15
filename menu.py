import random

def choose_word1():
    with open("palavras1.txt", "r") as file:
        words = file.readlines()
    return random.choice(words).strip().lower()

def choose_word2():
    with open("palavras2.txt", "r") as file:
        words = file.readlines()
    return random.choice(words).strip().lower()

def choose_word3():
    with open("palavras3.txt", "r") as file:
        words = file.readlines()
    return random.choice(words).strip().lower()

def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    return display

print('----------------------------------------------')
print('__________BEM VINDO AO JOJO DA FORCA__________')
print('----------------------------------------------')
print()

while True:
    nome = input('Digite seu nickname: ')
    print()
    
    tuto = input('Sabe como jogar? s:sim n:não ')

    if tuto == 's':
        print()
        print('certo...')
        print()
        
        if  tuto == 'n':
            print('_______Tutorial_______')
            print(f'Olá {nome}, o jogo da forca se baseia em uma palavra')
            print('secreta e aleatória. Você deve descobrir a palavra')
            print('secreta chutando uma letra ou fazendo um palpite de qual')
            print('é a palavra secreta.')
            print()
            print('A cada letra ou palpite errado, um membro do jogador é')
            print('exposto na forca (cabeça, torso, pernas e braços). Quando')
            print('todos os membros estiverem na forca, você perde.')

            print()
        opc = input('Começar jogo? s:sim n:não ')

        if opc == 's':
            dificuldade = input('Escolha a dificuldade: '
                                'fácil(1), difícil(2), IMPOSSIVEL(3): ')
            if dificuldade == '1':
                print('Jogo na dificuldade 1')
                word = choose_word1()
            elif dificuldade == '2':
                print('Jogo na dificuldade 2')
                word = choose_word2()
            elif dificuldade == '3':
                print('Jogo na dificuldade 3')
                word = choose_word3()
            else:
                print('Digite uma dificuldade válida.')

            print('Começar jogo...')
            
            guessed_letters = []
            attempts = 6

            while attempts > 0:
                print("\nPalavra: ", display_word(word, guessed_letters))
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
                else:
                    print("Letra correta!")

                if "_" not in display_word(word, guessed_letters):
                    print("\nParabéns! Você adivinhou a palavra: ", word)
                    break

                if attempts == 0:
                    print("\nVocê perdeu! A palavra era: ", word)
            continue


        else:
            print('Digite a opção corretamente.')
            break