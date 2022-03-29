import random
import unicodedata

def read_file(rute:str) -> list:
    """Reads file and create a list with all the words from it

    Returns:
        list: all words in file
    """
    try:
        with open(rute, 'r', encoding="utf-8") as f:
            # word_list = f.readlines()
            return [i.strip('\n') for i in f.readlines()]
    except FileNotFoundError as fnf:
        print(fnf)


def choose_random_word(word_list: list) -> str:
    """Choose a random word from a list

    Args:
        list: list of word from wich to choose from

    Returns:
        str: random word from a list
    """
    try:
        assert isinstance(word_list, list)
        return random.choice(word_list)
    except ValueError as err:
        print(err)
    except AssertionError('El argumento introducido debe ser una lista') as ae:
        print(ae)


def normalize_word(word:str) -> str:
        """Removes the accents from the provided string.
        
        Args:
            string: String to be normalized
        
        Returns:
            str: normalized string
        """
        assert isinstance(word, str), 'The parameter should be a string.'

        return unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore').decode().upper()



def get_initial_string(word_to_guess: str):
    characters = len(word_to_guess)
    return(list('_' * characters))

def print_guess(word_to_guess: list):
    for char in word_to_guess:
        print(char, end=' ')