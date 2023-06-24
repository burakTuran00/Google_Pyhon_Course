import bcrypt

def encrypt_password(password):
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password.decode('utf-8')

def verify_password(password, hashed_password):
    # Check if the password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Example usage
password = input("Enter your password: ")

# Encrypt the password
hashed_password = encrypt_password(password)

print("Hashed password:", hashed_password)

# Verify the password
password_to_check = input("Enter the password to check: ")

if verify_password(password_to_check, hashed_password):
    print("Password is correct!")
else:
    print("Password is incorrect!")
