def is_valid_email(email):
    return "@" in email and "." in email.split("@")[-1]

email = input("Enter an email: ")
if is_valid_email(email):
    print("True")
else:
    print("False")
    