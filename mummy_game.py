import time

import random

treasure_list = ['scarab', 'staff']


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You are an archaeologist.")
    print_pause("You have been sent to a dig at the Egyptian pyramids.")
    print_pause("You enter one of the pyramids.")


def choose_door(items):
    print_pause("To your left is a glittering gold door "
                "encrusted with jewels. "
                "To your right is a simpler-looking wooden door.")
    door = input("Press 1 to open the left door. "
                 "Press 2 to open the right door.")
    if door == "1":
        mummy_room(items)
    if door == "2":
        treasure_room(items)
    else:
        print_pause("Sorry, I don't understand.")
        choose_door(items)


def treasure_room(items):
    treasure_item = random_choice(treasure_list)
    items.append(treasure_item)
    if "scarab" in items:
        print_pause("You already got the silver scarab "
                    "from the treasure chest. "
                    "There is nothing more to do here.")
        choose_door(items)
    elif "staff" in items:
        print_pause("You already got the golden staff "
                    "from the treasure chest. "
                    "There is nothing more to do here.")
    else:
        print_pause("In this room is an ornate silver treasure chest. "
                    "You open the chest and pick up a silver scarab."
                    "You leave the room.")
        items.append("scarab")
        choose_door(items)


def you_win():
    play_again = input("You won the game. Would you like to play again? "
                       "Please enter Y or N.")
    if play_again == "Y":
            play_game()
    elif play_again == "N":
            print_pause("Thanks for playing. Have a great day!")
            exit()
    else:
            print_pause("Sorry, I don't understand.")
            you_win(items)


def mummy_room(items):
    print_pause("In this room lies a mummy. "
                "You walk up to the mummy to examine it more closely. "
                "Suddenly, it sits up. The mummy is alive!")
    fight = input("Press 1 to fight the mummy. "
                  "Press 2 to run away.")
    if fight == "1":
        if "scarab" in items:
            print_pause("Your silver scarab comes to life. "
                        "The mummy now sees you as a friend. "
                        "The mummy goes back to sleep. "
                        "You can now safely search the room "
                        "for more treasures!")
            you_win(items)
        elif "staff" in items:
            print_pause("You hold up the golden staff you found "
                        "in the treasure chest! "
                        "The mummy now sees you as a friend. "
                        "The mummy goes back to sleep. "
                        "You can now safely search the room "
                        "for more treasures!")
        else:
            print_pause("The mummy swings right at your head! "
                        "Fortunately, you're able to duck "
                        "just in time and run out the door.")
            choose_door(items)

    elif fight == "2":
        print_pause("You made it out of the mummy's room alive!")
        choose_door(items)

    else:
        print_pause("I'm sorry, I don't understand.")
        mummy_room(items)


def play_game():
    items = []
    intro()
    choose_door(items)


play_game()
