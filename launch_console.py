print("Welcome to the Launch Console!")

name = input("\nWhat is your name? ")
print(f"\nHi, {name}!")

running = True

while running:
    print("\n1) About me\n2) My goals\n3) Fun fact\n4) Exit\n")
    choice = input("Choose one(1-4): ")
    
    if choice == "1":
        print("I joined Code2College to improve my coding skills and explore a career in computer science.")
    elif choice == "2":
        print("My goal is to pass Elite 101 with high marks and perfect attendance.")
    elif choice == "3":
        print("A fun fact about me is that math is my favorite core subject.")
    elif choice == "4":
        running = False
    else:
        print("Pick a number from 1-4.")
