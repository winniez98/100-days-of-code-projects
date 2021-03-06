# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

# read in names
with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

# read in letter
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

for name in names:
    name_clean = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{name_clean}.txt", mode="w") as ready_letter:
        ready_letter.write(letter.replace(PLACEHOLDER, name_clean))

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
