# Mystery in the Dark Forest Adventure Game
# This program includes multiple scenarios and handles user choices through nested if statements.
# It features three levels of choices, with hidden choices and varied outcomes.

def start_game():
    print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT.")
    print("Which one do you want to pick up? (MATCH or FLASHLIGHT)")
    choice = input().lower()

    if choice == "match":
        print("You pick up the match and strike it, illuminating the forest.")
        print("Suddenly, a large grizzly bear appears. Do you want to RUN or HIDE BEHIND A TREE?")
        bear_choice = input().lower()
        
        if bear_choice == "run":
            print("You run as fast as you can and escape the bear. You find a safe clearing. You win!")
        elif bear_choice == "hide behind a tree":
            print("You hide behind a tree, but the bear sniffs around and finds you. You lose!")
        else:
            print("Invalid choice! Please choose either RUN or HIDE BEHIND A TREE.")

    elif choice == "flashlight":
        print("You pick up the flashlight and turn it on. The pathway is lit, but you hear a noise off to the side.")
        print("Do you want to FOLLOW THE PATH, LOOK IN THE TREES, or TURN OFF THE FLASHLIGHT?")
        flashlight_choice = input().lower()
        
        if flashlight_choice == "follow the path":
            print("You follow the path and discover a hidden treasure. You win!")
        elif flashlight_choice == "look in the trees":
            print("You look in the trees and find a mysterious creature that leads you deeper into the forest. You lose!")
        elif flashlight_choice == "turn off the flashlight":
            print("You turn off the flashlight, but now you can't see anything. You get lost! You lose!")
        else:
            print("Invalid choice! Please choose either FOLLOW THE PATH, LOOK IN THE TREES, or TURN OFF THE FLASHLIGHT.")
    
    else:
        print("Invalid choice! Please choose either MATCH or FLASHLIGHT.")

# Start the game
start_game()