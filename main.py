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

#logic 
game= [rock, paper, scissors]
computer_choose=random.choice(game)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n" ))
# Add the rest of your code logic here with proper indentation
if user_choice>=3 or user_choice<0:
  print("you entered an invalid number, you lose")
else:
    if user_choice==0 and computer_choose==rock:
        print(f"you choose rock: \n {rock} \n computer choose rock: \n {rock} \n its a draw")
    elif user_choice==0 and computer_choose==paper:
        print(f"you choose rock: \n {rock} \n computer choose paper: \n {paper} \n you lose")
    elif user_choice==0 and computer_choose==scissors:
       print(f"you choose rock: \n {rock} \n computer choose scissors: \n {scissors} \n you win") 
    elif user_choice==1 and computer_choose==rock:
        print(f"you choose paper: \n {paper} \n computer choose rock: \n {rock}\n you win")
    elif user_choice==1 and computer_choose==paper:
        print(f"you choose paper: \n {paper} \n computer choose paper: \n {paper}\n its a draw")
    elif user_choice==1 and computer_choose==scissors:
        print(f"you choose paper: \n {paper} \n computer choose scissors: \n {scissors}\n you lose ")
    elif user_choice==2 and computer_choose==rock:
        print(f"you choose scissors: \n {scissors} \n computer choose rock: \n {rock}\n you lose")
    elif user_choice==2 and computer_choose==paper:
        print(f"you choose scissors: \n {scissors} \n computer choose paper: \n {paper}\n you win")

    elif user_choice==2 and computer_choose==scissors:
        print(f"you choose scissors: \n {scissors} \n computer choose scissors: \n {scissors}\n its a draw")

