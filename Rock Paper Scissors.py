import random
items=["rock","paper","scissor"]
computer=random.choice(items)
user=input("Rock Paper or Scissor:").lower()
print("Computer Choose:",computer)
if user == computer:
    print("Match Draw...")
elif user == "rock" and computer == "scissor":
    print("User Win...")
elif user == "paper" and computer == "rock":
    print("User Win...")
elif user == "scissor" and computer == "paper":
    print("User Win...")
else:
    print("Computer Win...")
