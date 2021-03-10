import random


def biased_function():
    rvalue=random.random()
    if rvalue<0.1:
        return 6
    elif rvalue<0.4:
        return 5
    elif rvalue<0.5:
        return 4
    elif rvalue<0.7:
        return 3
    elif rvalue<0.9:
        return 2
    else:
        return 1



if __name__ == __main__:
    while True:
        choice=input('Press any key to roll the dice(q/Q to quit).')
        if choice == 'q' or choice =='Q': 
            break
        else:
            face=biased_function()
            print(f'\nYou got {face}')