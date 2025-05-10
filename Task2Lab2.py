import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

while True:
    name = input("Enter your name: ").strip()
    if name and not name.isdigit():
        break
    print("Invalid name. Please enter a valid name (non-empty and not numbers only).")

email = input("Enter your email: ").strip()
print("\n--- User Information ---")
print(f"Name: {name}")
print(f"Email: {email}")
if is_valid_email(email):
    print("Email is valid.")
else:
    print("Email is invalid.")
