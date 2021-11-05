import random

import os
os.system('cls' if os.name == 'nt' else 'clear')

def rockpaperscizors():

    while True:
        response = input('What would you like to choose? 1 for "rock", 2 for "paper" or 3 for "scizors". To end type "I quit" ')
        if response.lower() == 'i quit':
            print("Thank you for playing")
            break
        elif response not in ['1','2','3']:
            print('please select a valid choice')

        else:
            computerChoice = random.randint(0,2)
            playSet = ['Rock','Paper','Scizors']
            print(f'You play {playSet[int(response) - 1]}. The computer plays {playSet[computerChoice]}')
            if int(response) == computerChoice + 1:
                print("Game Tied")
            elif int(response) - (computerChoice + 1) == 1 or int(response) - (computerChoice + 1) == -2:
                print('You Win')
            else:
                print('You Lose')

rockpaperscizors()