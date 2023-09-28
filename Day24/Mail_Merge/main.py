
with open("Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

with open("Input/Names/invited_names.txt") as data:
    names = data.readlines()

for name in names:
    stripped_name = name.strip()
    letter = starting_letter.replace("[name]", stripped_name)
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final_letter:
        final_letter.write(letter)
