from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key()
    try:
        filekey = open('filekey.key','wb')
        filekey.write(key)
        filekey.close()
        return key
    except:
        key = ''
        filekey = open('filekey.key','rb')
        for i in filekey:
            key = i.strip('\n')
            return key
        filekey.close()
def enc_algo():
    fernet = Fernet(create_key())
    return fernet

def file_encryption(File_path):
    fernet = enc_algo()
    with open(File_path,'rb') as file:
        file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)
    with open(File_path,'wb') as file:
        file.write(encrypted_data)



if __name__ == "__main__":
    File_path = # Path to file to be encrypted
    file_encryption(File_path)