import textdistance
import random

def ask(prompt: str, valid: list = None) -> str:
    guess = input(prompt,)
    if valid:
        while not guess in valid:
            guess = input(prompt,)
        else:
            return guess
    else:
        return guess

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

def bullscows(guess: str, secret: str):
    bulls = textdistance.hamming.similarity(guess, secret)
    cows = textdistance.sorensen(list(guess), list(secret)) * len(secret) - bulls
    return bulls, int(cows)

def gameplay(ask: callable, inform: callable, words):
    secret = random.choice(words)
    print(secret)
    tries = 0
    while True:
        guess = ask("Введите слово: ", words)
        tries += 1
        b, c = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", b, c)
        if b == len(secret):
            return tries

