import random
import string
import hashlib

def generate_password(length, uppercase, lowercase, numbers, symbols):
    """Function to generate random password of given length and complexity"""
    if length <= 0 or (not uppercase and not lowercase and not numbers and not symbols):
        return None
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = []
    if uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if numbers:
        password.append(random.choice(string.digits))
    if symbols:
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)

    return ''.join(password)

try:
    length = int(input("Masukkan panjang password yang diinginkan: "))
    if length < 1:
        raise ValueError("Panjang password harus lebih dari 0.")
except ValueError as e:
    print("Input panjang password tidak valid:", e)
    exit()

uppercase = input("Termasuk huruf besar? (y/n): ").lower() == 'y'
lowercase = input("Termasuk huruf kecil? (y/n): ").lower() == 'y'
numbers = input("Termasuk angka? (y/n): ").lower() == 'y'
symbols = input("Termasuk simbol? (y/n): ").lower() == 'y'

password = generate_password(length, uppercase, lowercase, numbers, symbols)

if password:
    print("Password yang dihasilkan adalah:", password)

    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    print("Hashed Password:", hashed_password)
else:
    print("Tidak dapat menghasilkan password yang memenuhi kriteria yang diminta.")
