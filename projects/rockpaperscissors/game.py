import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

actions = [rock, paper, scissors]
usr, drw, comp=0,0,0

def game():
    user_choice = int(input("Enter your choice 0(rock) / 1(paper) / 2(scissors): "))
    global actions, comp, usr, drw
    try:
        print(f"\nYou Chose\n{actions[user_choice]}")

        comp_choice = random.randint(0,2)
        print(f"Computer Chose\n{actions[comp_choice]}")

        if user_choice == 0 and comp_choice == 1:
            print("You lose")
            comp+=1
        elif user_choice == 1 and comp_choice == 2:
            print("You lose")
            comp+=1
        elif user_choice == 2 and comp_choice == 0:
            print("You lose")
            comp+=1
        elif user_choice == comp_choice:
            print("It's a draw")
            drw+=1
        else:
            print("You Win!")
            usr+=1
    except IndexError:
        print('Choose correct value!')
        global times
        times+=1




print('Welcome to the game of rock, paper and scissors.')
try:
    times=int(input('\nHow many times you want to play the game?: '))
    while times!=0:
        game()
        times-=1
    print(f'----Results----\n\nUser Wins: {usr}\nComputer Wins: {comp}\nDraw: {drw}\n---------------')
except Exception(e):
    print('Please provide a valid value!')
    print(e)