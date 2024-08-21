# # Opening and reading the file.
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)
#     # file.close() # Use this just when openin the file like this: f = open("my_file.txt")

# # Edit the file
# Mode: w - Deletes everything and adds new text. If does not exit, will create a new one.
# Mode: a - Adds new text to the .txt file.
# with open("new_file.txt", mode="w") as file:
#     file.write("\nNew text")

# Creating personalized letters.
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter_content = (
        starting_letter.read()
    )  # Lee todo el contenido de la carta una sola vez

    for name in names:
        name = name.strip()
        with open(
            f"Output/ReadyToSend/{name}.txt",
            mode="w",
        ) as new_letter:
            personalized_letter = letter_content.replace(
                "[name]", name
            )  # Reemplaza el marcador con el nombre
            new_letter.write(
                personalized_letter
            )  # Escribe el contenido personalizado en el archivo
