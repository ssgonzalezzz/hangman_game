from process import *
from os import  system

def run():
    FILE_RUTE = 'files/data.txt'
    lives = 5
    word_list = read_file(FILE_RUTE)
    word = normalize_word(choose_random_word(word_list))
    system('clear')
    guess = (get_initial_string(word))

    while True:
        try:
            if guess == list(word):
                system('clear')
                print(f'Ganaste! La palabra que lograste adivinar es {word}')
                input()
                break
            if lives == 0:
                system('clear')
                print('Perdiste')
                input()
                break
            system('clear')
            print(f'Tienes {lives} vidas')
            print_guess(guess)
            print('\n')
            # print(word)
            letra = input('Intenta con una nueva letra: ').upper()
            if len(letra) != 1:
                raise Exception('El argumento introducido debe ser una letra')
            damage = False
            for indx, char in enumerate(word):
                # print(indx, char)
                if letra == char:
                    guess[indx] = letra
                    damage = True
            if damage == False:
                lives -= 1
        except Exception as ex:
            print(' ')
            print(ex)
            input('Presiona cualquier tecla para continuar')

    

if __name__ == '__main__':
    run()