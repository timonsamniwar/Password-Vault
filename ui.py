def head():
    print("PASSWORD GENERATOR & VAULT")

def menu():
    print()
    print("1. Generate Password")
    print("2. Add Vault Entry")
    print("3. View Vault")
    print("4. Search Vault")
    print("5. Update Entry")
    print("6. Delete Entry")
    print("7. Reveal Password")
    print("8. Password History")
    print("9. Save Vault")
    print("10. Exit")


def get_choice():
    return input("Enter your choice: ").strip()


def ask_length(a=14):
    raw = input("Password length (8-64) [",a,"]: ")
    if not raw:
        return a
    try:
        length = int(raw)
    except ValueError:
        print("Invalid number, using default.")
        return a
    if not 8 <= length <= 64:
        print("Out of range, using default.")
        return a
    return length