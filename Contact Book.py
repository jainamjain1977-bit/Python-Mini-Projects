contacts=[];
while True:
    print("1.Add Contact");
    print("2.View Contact");
    print("3.Search Contact");
    print("4.Delete Contact");
    print("5.Exit");
    choice = int(input("Enter your choice:"));
    if choice==1:
        name=input("Enter your name:");
        number=input("Enter number:");
        contact={"name":name,"number":number};
        contacts.append(contact);
        print("Contact Saved!!!");
    elif choice==2:
        if len(contacts)==0:
            print("No Contact Yet!!!");
        else:
            for i in range(len(contacts)):
                print(i+1,contacts[i]["name"],contacts[i]["number"]);
    elif choice==3:
        search_name = input("enter name to search:");
        found = False;
        for c in contacts:
            if c["name"].lower()==search_name.lower():
                print(c["name"],"_",c["number"]);
                found = True;
            if not found:
                print("Contact not found!!!");
    elif choice==4:
        num=int(input("enter the contact number(position) to delete:"));
        if num>0 and num<=len(contacts):
            removed=contacts.pop(num-1);
            print("Deleted",removed["name"]);
        else:
            print("Invalid selection!!!");
    elif choice==5:
        print("Good bye!!!");
        break;
    else:
        print("Invalid Choice Try again!!!");
    
        
        
