import pyAesCrypt
from getpass import getpass

password = getpass(prompt='Password: ')

# encrypt
pyAesCrypt.encryptFile('file.txt', 'file.txt.aes', password)

# decrypt
pyAesCrypt.decryptFile('file.txt.aes', 'new_file.txt', password)
