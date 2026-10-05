import pyjokes
joke = pyjokes.get_joke()
print("Joke of the moment :");
print(joke);
print();
print("Here are a few more :");
count = 1;
while count <= 5:
    print(str(count)+"."+pyjokes.get_joke());
    count += 1;
print();
print("Bonus check Norris joke :");
print(pyjokes.get_joke(category="chuck"));
    
