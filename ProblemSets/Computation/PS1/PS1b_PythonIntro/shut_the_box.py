# shut_the_box.py

# import packages
import box
import sys
import time
import random

# define function to check input
def check(elim):
    elim = box.parse_input(elim, numbers)  
    while len(elim)==0 or sum(elim)!=roll:
        print("Invalid input\n")
        timeleft = eval(sys.argv[2]) - time.time() + start
        print("Seconds left: ", max(round(timeleft,2),0))
        if timeleft <= 0:
            print("Time's up, game over!\n")
            return 0
        elim = input("Numbers to eliminate: ")
        elim = box.parse_input(elim, numbers)
    return elim

# check number of command line arguments
if len(sys.argv) != 3:
    print("Type the player's name and the time limit in seconds as command arguments to play")
    
# start the game
numbers = list(range(1,10))
start = time.time()

while True:
    # calculate seconds left
    timeleft = eval(sys.argv[2]) - time.time() + start
    
    # roll the 2 dice
    roll1 = random.randint(1,6)
    if sum(numbers) > 6:
        roll2 = random.randint(1,6)
    else:
        roll2 = 0
    roll = roll1 + roll2
    
    print("Numbers left: ", numbers)
    print("Roll: ", roll)
    if not box.isvalid(roll, numbers):
        print("Game over!\n")
        break
    print("Seconds left: ", max(round(timeleft,2),0))
    if timeleft <= 0:
        print("Time's up, game over!\n")
        break
    
    elim = input("Numbers to eliminate: ")
    elim = check(elim)
    if elim==0:
        break
    
    numbers = [x for x in numbers if x not in elim]
    print("")
    
    if sum(numbers)==0:
        break      
end = time.time()

print("Score for player ", sys.argv[1], ": ", sum(numbers), " points")
print("Time played: ", min(round(end-start,2), eval(sys.argv[2])), "seconds")
if sum(numbers)==0:
    print("Congratulations!! You shut the box!")
else:
    print("Better luck next time >:)")