import os
import random

secret_number = random.randint(1,1000)

value = secret_number
value_guessed = False


taunts_low = [
    "Bro that's tiny... try bigger",
    "My grandma guesses higher than that",
    "Did you just guess with your eyes closed?",
    "Even my dog knows it's higher"
]

taunts_high = [
    "Chill bro, that's massive!",
    "You trying to break the scale?!",
    "Lower... like your standards apparently",
    "I said number, not your credit card bill"
]

print ("Try and guess the mystery value!!!")
while value_guessed == False:
    try:
        input1 = input("Enter Your Guess: ")
        input_value = int(input1)
        
        if value == input_value:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"YOU GUESSED IT!!! NICE JOB! The mystery value was {value}\n")
            input("Press Enter to exit...")
            value_guessed = True
        elif value < input_value:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(random.choice(taunts_high))
            print(f"\nYour value is too L A R G E! Try something lesser than {input1}\n")
        elif value > input_value:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(random.choice(taunts_low))
            print(f"\nYour value is too S M A L L! Try something greater than {input1}\n")
    except ValueError:
        print("That's not a valid number. Please try again.\n")
        print(f"\n...does {input1} really look like a number to you?")
            

    


