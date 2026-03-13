import sys
import os
import hashlib
import base64
from cryptography.fernet import Fernet


def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)


def encrypt_file(file_path, password):

    if not os.path.exists(file_path):
        print("File not found!")
        return

    key = generate_key(password)
    f = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = f.encrypt(data)

    new_file = file_path + ".locked"

    with open(new_file, "wb") as file:
        file.write(encrypted_data)

    os.remove(file_path)

    print("File encrypted successfully.")
    print("Output:", new_file)


def decrypt_file(file_path, password):

    if not os.path.exists(file_path):
        print("File not found!")
        return

    key = generate_key(password)
    f = Fernet(key)

    try:

        with open(file_path, "rb") as file:
            data = file.read()

        decrypted_data = f.decrypt(data)

        original_file = file_path.replace(".locked", "")

        with open(original_file, "wb") as file:
            file.write(decrypted_data)

        os.remove(file_path)

        print("File decrypted successfully.")
        print("Output:", original_file)

    except Exception:
        print("Wrong password or corrupted file!")


def show_usage():

    print("\nUsage:")
    print("Lock file:")
    print("python setup.py lock <file> <password>\n")

    print("Unlock file:")
    print("python setup.py unlock <file.locked> <password>\n")


def main():

    if len(sys.argv) < 4:
        show_usage()
        return

    mode = sys.argv[1]
    file_path = sys.argv[2]
    password = sys.argv[3]

    if mode == "lock":
        encrypt_file(file_path, password)

    elif mode == "unlock":
        decrypt_file(file_path, password)

    else:
        show_usage()


if __name__ == "__main__":
    main()