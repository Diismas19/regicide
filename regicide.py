from functions import *

input("""Welcome leader, let's begin Operation Regicide.
(Press 'Enter' to start the game.)
""")

regicide = Game()

while True:
    regicide.play_card()
    if regicide.alive == False:
        print('The operation failed!')
        break
    regicide.check_royal_death()
    if len(regicide.castle) == 0:
        print(f'Congratulations leader, we won!')
        input()
        if regicide.jester == 2:
            print('And it was a Golden victory, you are one of the greatest leaders in the realm.')
        if regicide.jester == 1:
            print('And it was a Silver victory, it was a good operation.')
        if regicide.jester == 0:
            print("And it was a Bronze victory, you commited some mistakes, but in the end the operation was a sucess.")
        break
    if regicide.alive == False:
        print('The operation failed!')
        break