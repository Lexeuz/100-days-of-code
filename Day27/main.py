from cryptography.fernet import Fernet

def load_key():
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


'''
def write_key():
    key = Fernet.generate_key()                                              
    with open("key.key", "wb") as key_file:
        key_file.write(key)


write_key()'''




def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user, passw = data.split("|")
            print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f: # Closes the file automatically.
        # w -> Write / Overwrite a file, clear and make entire new.
        # r -> Read, just read and open file.
        # a -> Add something to the end of an existing file or create a new one.
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Whould like to add a new password or view existing ones (view, add), press 'q' to quit.?\n")
    if mode == "q":
        break

    if mode == "view":
        print("")
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue