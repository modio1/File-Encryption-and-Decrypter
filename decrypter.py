from cryptography.fernet import Fernet
def get_key():
    try:
        fernet = ''
        key_file = open('filekey.key','rb')
        for key in key_file:
            fernet = Fernet(key)
        return fernet
    except:
        print("Please move the key_file.key into the same folder as the decrypter.")
        print("Otherwise without a key you're pretty much fucked.")
        key = input("Enter your key:")
        fernet = Fernet(key)
        return fernet

def decrypt_file(File_path):
    fernet = get_key()
    with open(File_path,'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(File_path,'wb') as dec_file:
        dec_file.write(decrypted)


if __name__ == "__main__":
    File_path = # Path to the file to be decrypted
    decrypt_file(File_path)