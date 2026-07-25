# script which gets user to submit a sentence and then manipulates it in different forms
# user input
user_input = "" 

# validate with a while loop to make sure the input is not just white space or empty
while user_input.isspace() or user_input == "":
    user_input = input("Enter a sentence: ")

    # conditional if it's still not valid - notify user
    if user_input.isspace() or user_input == "":
        print("Invalid sentence. Please retry")

# print uppercase
print(f"Uppercase: {user_input.upper()}")
# print reverse - reversed function gives iterable, join it to put it together
reversed_input = "".join(reversed(user_input))
print(f"Reversed: {reversed_input}")

# count vowels - make a set for O(1) lookups
vowels_set = set('aeiouAEIOU')

# loop the string and add a count
vowel_count = 0

for char in user_input:
    if char in vowels_set:
        vowel_count += 1

print(f"Vowel Count: {vowel_count}")

# replace space with hyphen with replace menthod
new_sent = user_input.replace(" ", "-")
print(f"Hyphen sentence: {new_sent}")