from process import *
from os import  system

def run():
    FILE_RUTE = 'files/data.txt'

    word_list = read_file(FILE_RUTE)
    word = normalize_word(choose_random_word(word_list))
    system('clear')
    guess = (get_initial_string(word))
    while True:
        if guess == list(word):
            break
        system('clear')
        print_guess(guess)
        print('\n')
        # print(word)
        letra = input('Intenta con una nueva letra: ').upper()
        for indx, char in enumerate(word):
            # print(indx, char)
            if letra == char:
                guess[indx] = letra
    

    system('clear')
    print(f'Ganaste! La palabra que lograste adivinar es {word}')
    input()

if __name__ == '__main__':
    run()