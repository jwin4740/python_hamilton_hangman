from random import randint
import time

WORD_LIST = ["Alexander Hamilton", "My Shot", "The Story of Tonight", "The Schuyler Sisters", "Farmer Refuted",
             "Right Hand Man", "Helpless", "Satisfied", "Wait for It", "Stay Alive", "Ten Duel Commandments",
             "Meet Me Inside", "That Would Be Enough", "Guns and Ships", "History Has Its Eyes On You",
             "Dear Theodosia", "Take a Break", "Say No to This", "The Room Where It Happens",
             "Schuyler Defeated", "Washington On Your Side", "One Last Time", "I Know Him", "The Adams Administration",
             "We Know", "Hurricane", "The Reynolds Pamphlet", "Burn", "Blow Us All Away", "Your Obedient Servant",
             "Best of Wives and Best of Women", "The World Was Wide Enough"]
LETTER_UNDERSCORE = " _ "
SPACE = "    "

guesses_left = 7
game_over = False
did_win = False

current_word = ""
letter_dict = {}


def evaluate_guess(word, guess):
    global letter_dict, guesses_left

    correct = False
    for character in current_word:
        upper_guess = guess.upper()
        upper_character = character.upper()
        if upper_guess == upper_character:
            correct = True
            letter_dict[upper_character]["guessed"] = True

    if correct != True:
        guesses_left = guesses_left - 1
        print("Incorrect guess you have " + str(guesses_left) + " left\n")


def user_guess():
    global current_word
    guess = input("Guess a letter: ")
    evaluate_guess(current_word, guess)
    draw_board(current_word)


def draw_board(word):
    for character in word:
        uppercase_character = character.upper()
        if uppercase_character == " ":
            print(SPACE, end="")

        elif letter_dict[uppercase_character]["guessed"] == True:
            print(uppercase_character + " ", end="")
        else:
            print(LETTER_UNDERSCORE, end="")
    print("\n")


def fill_letter_dict(word):
    global letter_dict

    for character in word:
        uppercase_character = character.upper()
        character_attributes_dict = {
            "character": "",
            "guessed": False
        }
        if uppercase_character not in letter_dict and uppercase_character != " ":
            character_attributes_dict["character"] = uppercase_character
            letter_dict[uppercase_character] = character_attributes_dict


def get_random_word():
    index = randint(0, len(WORD_LIST) - 1)
    random_word = WORD_LIST[index]
    return random_word


def setup_game():
    global current_word

    # get word
    current_word = get_random_word()
    fill_letter_dict(current_word)
    draw_board(current_word)


def trigger_loss():
    time.sleep(1)
    while True:
        print("YOU THREW AWAY YOUR SHOT\n")
        time.sleep(0.2)


def game_ends():
    global did_win
    if did_win == True:
        print("\n\nYOU WIN!!!!\n\n\n")
        exit(0)
    else:
        print("SORRY SUCKER, YOU LOSE; NOW ENJOY THIS INFINITE WHILE LOOP...\n")
        time.sleep(2.5)
        trigger_loss()


def check_game_over():
    global guesses_left, did_win, game_over

    if guesses_left == 0:
        return True

    for key in letter_dict:
        if letter_dict[key]["guessed"] == False:
            return False
    did_win = True
    return True


def start_game():
    global game_over, guesses_left
    print("WELCOME TO HANGMAN\n-------------------\n")
    setup_game()
    while game_over == False:
        user_guess()
        game_over = check_game_over()

    game_ends()


start_game()
