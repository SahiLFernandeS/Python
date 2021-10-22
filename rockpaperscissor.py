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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock,paper,scissor]

user_input = int(input('Type 0 for "Rock", 1 for "Paper" and 2 for "Scissor"'))


if user_input > 3 or user_input < 0:
  print("Invalid input, you lose")
else:
  print(f'You :')
  print(game[user_input])
  computer_input = random.randint(0,2)
  print(f"Computer :")
  print(game[computer_input])

  if user_input == 0 and computer_input == 2:
    print('You win!')
  elif user_input < computer_input:
    print('You lose')
  elif user_input == 1 and computer_input == 0:
    print("You win!")
  elif user_input == 2 and computer_input == 0:
    print("You lose")
  elif user_input == 2 and computer_input == 1:
    print("You win!")
  elif user_input == computer_input:
    print("Its a draw")
  else:
    print("invalid input, you lose")