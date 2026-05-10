print("Welcome to the Magic Forest")
user_direction=input("Which direction do you want to go? (North, South): ")
user_direction.lower()
if user_direction == "south":
    river_or_path = input("You see a river and a path. Which one do you choose? (River, Path): ")
    river_or_path.lower()
    if river_or_path == "path":
        choose_option = input("Chose one (Fairy, Ogre, Elf): ")
        if choose_option == "fairy" or choose_option == "ogre":
            print("GAME OVER!")
        elif choose_option == "elf":
            print("Congratulations! You Win!")
        else:
            print("Invalid input. Please choose either 'Fairy', 'Ogre', or 'Elf'.")
            
    elif river_or_path == "river":
        print("You have crossed the river!")
    else:
        print("Invalid input. Please choose either 'River' or 'Path'.")
elif user_direction == "north":
    print("GAME OVER!")
else:
    print("Invalid input. Please choose either 'North' or 'South'.")