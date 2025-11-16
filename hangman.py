# create your word list
# randomly choose a word from the list you have created 
# ask the user to guess a letter
# bonus make the program take the input from the user and make it lowecase
# check is the letter is in the word


import random
print("hello user..!")
lst = ["mango","grape","kiwi","guawa","lemon","banana"]

word = random.choice(lst)
guess = input("Guess a letter : ").lower()

if guess in word:
    print("letter is in word")
else:
    print("Better luck next time")
