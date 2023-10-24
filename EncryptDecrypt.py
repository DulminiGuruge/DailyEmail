from cryptography.fernet import Fernet

"""
Generating the Key-
Fernet is an implementation of symmetric authenticated cryptography; 
let's start by generating that key and writing it to a file:
The Fernet.generate_key() function generates a fresh fernet key, 
you really need to keep this in a safe place. If you lose the key, you will no 
longer be able to decrypt data that was encrypted with this key.

"""
def write_key():
    """
    Generates a key and save it into a file
    """
    
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


"""
 Function to load the key
 """       
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

"""
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
def encrypt(filename, key):
    #initializing the Fernet object with the given key
    f = Fernet(key)

    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()

    # encrypt data
    encrypted_data = f.encrypt(file_data)  

    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

"""
Decrypt a given file
we will use the decrypt() function instead of encrypt() on the Fernet object:
Given a filename (str) and key (bytes), it decrypts the file and write it
"""        
def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
  

#Test the class
# uncomment this if it's the first time you run the code, to generate the key
#write_key()
# load the key
key = load_key()
# file name
file = "configs.txt"
# encrypt it
#encrypt(file, key)
# decrypt the file
decrypt(file, key)