import random

def hangman():
    word_list = ['apple', 'orange', 'banana', 'pear']
    computer = "apple"
    attempts = 15
    user_attempt = 0
    user_input = []

    while user_attempt <= attempts:
        for i in computer:
            current_guess = str(input("Enter the letter: "))
            if current_guess != i:
                print(f"{current_guess} is wrong guess!")
            else:
                print("Your guess is right!")
                user_input.append(i)
                if len(computer) == len(user_input):

                 if sorted(computer) == sorted(user_input):
                    print(f"You entered{user_input}, you won!")
                    break
                 else: print(f"You entered{user_input}, you loose!")
                 

hangman() 