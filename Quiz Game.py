score = 0;
print("=== Quiz Game ===");
#Displaying the question and 4 options.
print("1). Who is the creater of python?");
print("A). Dennie Ratchie");
print("B). Bjarne Strustrup");
print("C). Guido Van Rossum");
print("D). Jamps gasling");
#Taking input from the user
answer = input("enter your choice(A/B/C/D):");
#checking if the answer is correct
if answer == "C" or answer == "c":
    print("correct! well done.");
    score += 1;
else:
    print("wrong! the correct answer is C");
    print("Guido Van Rossum");
