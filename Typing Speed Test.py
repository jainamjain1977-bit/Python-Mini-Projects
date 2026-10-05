import time
print(" Speed Typing Test!! ");
sentence = "abcdefghijklmnopqrstuvwxyz";
print("\n Type This Exactly... ");
print(sentence);
input("\n Press Enter To Start... ");
start = time.time();
typed = input("\nStar Typing... :");
end = time.time();
time_taken = round(end-start,2);
speed = round(len(sentence)/time_taken,2);
print("Time Taken : ",time_taken,"second");
print("Typing speed",speed,"letters/sec");
if(typed == sentence):
    print("Correct sentence Typed...");
else:
    print("Mistake Found...");

