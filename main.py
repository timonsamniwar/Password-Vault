from generator import generate_password
from security import show_strength
from ui import head, menu, get_choice, ask_length
from history import show_history
from vault import Vault


def run():
    head()
    vault = Vault()
    if not vault.login():
        print("Could not unlock the vault. Program closed.")
        return

    while True:
        menu()
        choice = get_choice()

        if choice == "1":
            password = generate_password(ask_length())
            print("Generated password:", password)
            show_strength(password)

        elif choice == "2":
            vault.add()

        elif choice == "3":
            vault.view()

        elif choice == "4":
            vault.search()

        elif choice == "5":
            vault.update()

        elif choice == "6":
            vault.delete()

        elif choice == "7":
            vault.reveal()

        elif choice == "8":
            show_history()

        elif choice == "9":
            vault.save()

        elif choice == "10":
            if vault.unsaved:
                if input("You have unsaved changes. Save before exit? (y/n): ").strip().lower() == "y":
                    vault.save()
            print("Thank you for using Password Vault.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    run()