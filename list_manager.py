# script to manage a list of integers with a text-based menu

# starter number list
num_list = [2, 4, 6, 8]

# set with the number choices
menu_set = set('abcdABCD')

# loop which won't exit until d is chosen
while True:
    try:
        # script opens with the menu
        menu_choice = input(f"Number Manager Menu: \n These are your numbers {num_list} \n A. Add Number \n B. Remove Number \n C. Display List \n D. Quit \n Enter your choice (A-D): ")

        # restart if it is NOT A-D
        if menu_choice not in menu_set:
            print(f"{menu_choice} is not a valid choice A-D. Try again.")
            continue
    except:
        # continue to run the loop again and the menu
        print(f"{menu_choice} isn't a valid number 1-5. Try again")
        continue

    # convert to upper anyways so it's easier behind the scenes
    choice_upper = menu_choice.upper()

    # for the code to get here it should have alredy been 1-5, so the else can just be the 5
    if choice_upper == 'A':
        # some try except logic that will check if it's an integer and reprompt if there are errors
        try:
            # get input and convert string to int
            num_to_add = int(input("Add an integer: "))

            # if it doesn't crash it'll add it
            num_list.append(num_to_add)

        # value error for it not being able to be converted to an integer
        except ValueError:
            print("The number you wrote is not an integer. Try again")

    elif choice_upper == "B":
        # protect for empty list - bring them back to menu
        if len(num_list) == 0:
            print("List is currently empty. Nothing to remove")
            continue

        # the try block will automatically check if it's first and integer and next in bounds, if it fails error message
        try:
            # if the list isn't empty then there's at least one
            if len(num_list) == 1:
                index_to_remove = int(input(f"Choose index 0: "))
            else:
                index_to_remove = int(input(f"Choose an index, 0 to {len(num_list) - 1}: "))

            num_list.pop(index_to_remove)

        # error for non-int input
        except ValueError:
            print("The index must be an integer. Try again")
        # error for wrong index
        except IndexError:
            print("The number you wrote is out of bounds. Try again")

        # some try except logic that will check if it's 0 to whatever
    elif choice_upper == "C":
        print(f"Displaying your current list: {num_list}")
    else:
        print("Exiting number list.")
        break