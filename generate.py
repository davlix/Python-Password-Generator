import random
import string
import hashlib

def generate_password(length, uppercase, lowercase, numbers, symbols):
    """Function to generate random password of given length and complexity"""
    # Validasi parameter masukan
    if length <= 0 or (not uppercase and not lowercase and not numbers and not symbols):
        return None

    # Memilih karakter yang akan digunakan dalam password
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    # Membuat password dengan karakter acak
    password = ''.join(random.choice(characters) for i in range(length))

    # Memastikan bahwa password memenuhi kriteria kompleksitas
    while not is_password_strong(password):
        password = ''.join(random.choice(characters) for i in range(length))

    return password

def is_password_strong(password):
    """Function to check if password is strong enough"""
    # Memeriksa minimal panjang password
    if len(password) < 8:
        return False

    # Memeriksa minimal jumlah karakter
    count_uppercase = sum(1 for c in password if c.isupper())
    count_lowercase = sum(1 for c in password if c.islower())
    count_numbers = sum(1 for c in password if c.isdigit())
    count_symbols = sum(1 for c in password if c in string.punctuation)
    if count_uppercase < 1 or count_lowercase < 1 or count_numbers < 1 or count_symbols < 1:
        return False

    # Memeriksa pengulangan karakter yang sama dalam password
    for i in range(len(password)-2):
        if password[i] == password[i+1] == password[i+2]:
            return False

    return True

# Mengambil input dari pengguna untuk panjang password dan kompleksitas yang diinginkan
length = int(input("Masukkan panjang password yang diinginkan: "))
uppercase = input("Termasuk huruf besar? (y/n): ").lower() == 'y'
lowercase = input("Termasuk huruf kecil? (y/n): ").lower() == 'y'
numbers = input("Termasuk angka? (y/n): ").lower() == 'y'
symbols = input("Termasuk simbol? (y/n): ").lower() == 'y'

# Memanggil fungsi untuk menghasilkan password acak
password = generate_password(length, uppercase, lowercase, numbers, symbols)

# Mencetak password yang dihasilkan
if password:
    print("Password yang dihasilkan adalah:", password)

    # Membuat hash password
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    print("Hashed Password:", hashed_password)
else:
    print("Tidak dapat menghasilkan password yang memenuhi kriteria yang diminta.")
