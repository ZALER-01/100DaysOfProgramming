import random as rnd
# import random module to suffle between words or select random words


word_list = ['Rituraj', 'Abhinav', 'Mukul','deepak']

choose_word = rnd.choice(word_list).lower()
print(choose_word)

#Ask user to guess a letter

guess = input('Guess a letter: ').lower()



