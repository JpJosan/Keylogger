from cryptography.fernet import Fernet

key="NuNWck8rdu6M0_GQCkGxhOSOvcUAfTD4ga5IMEkP8PU="

system_information_e="tempS.txt"
clipboard_information_e="tempC.txt"
keys_information_e="tempK.txt"

keys_information="decryptK.txt"
system_information="decryptS.txt"
clipboard_information="decryptC.txt"

file_path="C:\\OLD\\Projects\\Keylogger\\Project"
extend="\\"
file_merge=file_path+extend

encrypted_files=[file_merge+system_information_e, file_merge+clipboard_information_e, file_merge+keys_information_e]
decrypted_files=[file_merge+system_information, file_merge+clipboard_information, file_merge+keys_information]
count=0

for decrypting_file in encrypted_files:

    with open(encrypted_files[count], "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(decrypted_files[count], "wb") as f:
        f.write(decrypted)

    count += 1