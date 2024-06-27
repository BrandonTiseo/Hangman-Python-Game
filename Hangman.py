import random

#Index 0 = Empty Index 6 = Full
hangman_pictures = ['''
                       +-----+
                       |     |
                       |    
                       |    
                       |    
                       |_______ 
                    ''','''
                       +-----+
                       |     |
                       |    ( )
                       |    
                       |    
                       |_______ 
                    ''','''
                       +-----+
                       |     |
                       |    ( )
                       |     |
                       |    
                       |_______ 
                    ''','''
                       +-----+
                       |     |
                       |    ( )
                       |    /|
                       |    
                       |_______ 
                    ''','''
                       +-----+
                       |     |
                       |    ( )
                       |    /|\\
                       |    
                       |_______ 
                    ''','''
                       +-----+
                       |     |
                       |    ( )
                       |    /|\\
                       |    / 
                       |_______ 
                    ''','''
                       +-----+
                       |     |
                       |    ( )
                       |    /|\\
                       |    / \\
                       |_______ 
                       ''']
amount_wrong = 0
amount_correct = 0
guesses = []
game_word = []

def random_word_generator():
    random_num = random.randint(0,9999)
    with open("WordList.txt","r") as f1:
        wordList_lines = f1.readlines()
        random_word = list(wordList_lines[random_num])
        random_word.remove("\n")
        return(random_word)
def guess_checking(guess):
   global guesses
   global amount_wrong
   global amount_correct
   if guess.upper() in guesses or guess.lower() in guesses:
      print("You already guessed this letter!")
      return -1
   if guess in game_word:
      print("Correct!")
      amount_correct += game_word.count(guess)   
      guesses.append(guess.upper())
      return(0)
   else:
      print("Incorrect!")
      amount_wrong += 1
      guesses.append(guess.lower())
      return(1)
   

print("Welcome to Hangman!\n")
print(f"{hangman_pictures[6] : <20}") 

while True:
    try:
        help_choice = input("Would you like an explanation on how to play? (Y/N): \n")
    except(TypeError):
        print("INVALID INPUT - Please enter Y or N.")
    if help_choice == "Y" or help_choice == "y":
        print("- " * 30)
        print(f"{'Your goal is to guess all the letters in a randomly generated word within 6 turns. Each incorrect guess adds a body part to the hangman, acting as a visual representation of your incorrect guesses. Each correct guess will result in the letter being written everywhere it is found in the word.' : >20}")
        print("- " * 30)
    if help_choice == "N" or help_choice == "n":
        print("- " * 30)
        break

game_word = random_word_generator()
word_display = []
for letter in game_word:
   word_display.append("___")

while amount_wrong != 6 and amount_correct != len(game_word):

   print(hangman_pictures[amount_wrong])
   for count,letter in enumerate(game_word):
      for guess in guesses:
         if guess.lower() == letter and guess.isupper():
            word_display[count] = letter            

   word_display_string = ""
   for letter in word_display:
      word_display_string += letter + " "
   print("Guesses: " + str(guesses) + "\n" + 
         word_display_string)
   
   user_input = input("Enter a letter: ")
   guess_checking(user_input)


if amount_wrong == 6:
   print("- " * 30)
   print("You lost.")
if amount_correct == len(game_word):
   print("- " * 30)
   game_word_string = ""
   for letter in game_word:
      game_word_string += letter
   print("You guessed the word correctly! It was:\n" + game_word_string + "!")
   print(hangman_pictures[amount_wrong])
      
      
   
      
            
   
   
   

         
         