from password_utils import generate_password
import pyperclip

print("🔐 Password Generator 🔐")

length = int(input("Enter password length: "))
strength = input("Choose strength (weak / medium / strong): ").lower()

password = generate_password(length, strength)

print("\nGenerated Password:", password)

copy = input("Copy to clipboard? (y/n): ")
if copy == 'y':
    pyperclip.copy(password)
    print("✅ Password copied!")
