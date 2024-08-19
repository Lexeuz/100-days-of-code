# # Opening and reading the file.
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)
#     # file.close() # Use this just when openin the file like this: f = open("my_file.txt")

# # Edit the file
# Mode: w - Deletes everything and adds new text. If does not exit, will create a new one.
# Mode: a - Adds new text to the .txt file.
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text")
