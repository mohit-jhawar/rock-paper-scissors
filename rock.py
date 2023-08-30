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

#Write your code below this line 👇
import random
a = int(input("What do you chose? 0 for rock, 1 for paper and 2 for scissors. \n"))
b = [rock,paper,scissors]
print(b[a])
print("Computer chose:")
c = random.randint(0,2)
print(b[c])
if a==0:
  if c==0:
    print("Draw")
  elif c==1:
    print("You lose")
  else:
    print("You win")
elif a==1:
  if c==0:
    print("You win")
  elif c==1:
    print("Draw")
  else:
    print("You lose")
else:
  if c==0:
    print("You lose")
  elif c==1:
    print("You win")
  else:
    print("Draw")