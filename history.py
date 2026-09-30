import hashlib
from datetime import datetime

password_history = []


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def add_to_history(password):
    password_history.append({"hash": hash_password(password),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),})


def was_used(password):
    digest = hash_password(password)
    return any(item["hash"] == digest for item in password_history)


def show_history():
    print("PASSWORD HISTORY")

    if not password_history:
        print("No password history available.")
        return

    for i, item in enumerate(password_history, 1):
        print(i,". Hash: ",item['hash'])
        print(" Time: ",item['time'])