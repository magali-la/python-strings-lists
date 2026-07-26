# script to check if age is within a specific range
# define validator function w a custom error message
def validate_age(age):
    # set up rule for the accepted age range
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120, inclusive.")
    

# take user input first 
user_input = input("Enter age: ")

# this try/except/else block is to check first if its even an integer and raise a different custom error and exit if it doesn't pass
try:
    # this is the converted
    user_age = int(user_input)

except ValueError:
    print("Not a valid integer. Try again.")

# this is going to run if ther was no error while converting to integer
else:
    try:
        # should be an int by now call the function with the input
        validate_age(user_age)

        print("Age valid!")

    # take the custom range error
    except ValueError as error:
        print(f"{error}")