import getpass
import hashlib
import json
import os
from datetime import datetime

from generator import generate_password
from history import add_to_history, was_used
from security import show_strength
from ui import ask_length

vault_file = "vault.dat"
master_file = "master.dat"
max_attempts = 3

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def hash_master(password):
    return hashlib.sha256(password.encode()).hexdigest()

class Vault:
    def __init__(self):
        self.data = []
        self.master_hash = None
        self.unsaved = False

    def login(self):
        print("MASTER PASSWORD")

        if not os.path.exists(master_file):
            if not self.create_master():
                return False
        else:
            with open(master_file, "r", encoding="utf-8") as f:
                self.master_hash = f.read().strip()

            for attempt in range(1, max_attempts + 1):
                entered = getpass.getpass("Enter master password: ")
                if hash_master(entered) == self.master_hash:
                    break
                print("Wrong password ",(attempt/max_attempts),".")
            else:
                return False

        self.load()
        return True

    def create_master(self):
        print("No master password yet. Create one.")
        while True:
            first = getpass.getpass("Choose a master password: ")
            if not first:
                print("Master password cannot be empty.")
                continue
            if first != getpass.getpass("Confirm master password: "):
                print("Passwords do not match.")
                continue
            break

        self.master_hash = hash_master(first)
        with open(master_file, "w", encoding="utf-8") as f:
            f.write(self.master_hash)
        return True

    def load(self):
        if not os.path.exists(vault_file):
            return

        try:
            with open(vault_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Vault file could not be loaded. Starting with empty vault.")
            self.data = []

    def save(self):
        try:
            with open(vault_file, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=4)
            self.unsaved = False
            print("Vault saved to", vault_file)
        except OSError as e:
            print("Could not save vault:", e)

    def select(self):
        self.view()
        if not self.data:
            return None

        try:
            i = int(input("Enter entry number: ")) - 1
            if 0 <= i < len(self.data):
                return i
        except ValueError:
            pass

        print("Invalid entry number.")
        return None

    def add(self):
        print("ADD VAULT ENTRY")
        site = input("Website/App: ").strip()
        user = input("Username/Email: ").strip()

        if not site or not user:
            print("Website/App and Username/Email are required.")
            return
        
        generate = input("Generate password? (y/n): ").strip().lower()
        if generate == "y":
            password = generate_password(ask_length())
            print("Generated password:", password)
        else:
            password = getpass.getpass("Password: ")

        if not password:
            print("Password cannot be empty.")
            return

        if was_used(password):
            print("Warning: you have used this password before.")

        category = input("Category: ").strip() or "General"
        notes = input("Notes: ").strip()

        show_strength(password)
        add_to_history(password)

        self.data.append({"site": site, "user": user, "password": password,
            "category": category, "notes": notes,
            "created": now(), "modified": now(),})
        self.unsaved = True
        print("Entry added.")

    def view(self):
        if not self.data:
            print("Vault is empty.")
            return

        print("VAULT ENTRIES")
        for i, x in enumerate(self.data, 1):
            print(i,".", x['site'], "|", x['user'], "|", x['category'])

    def search(self):
        q = input("Search Website/App or Username/Email: ").strip().lower()
        found = False

        for i, x in enumerate(self.data, 1):
            if q in x["site"].lower() or q in x["user"].lower():
                print(i,".", x['site'])
                print("   Username:", x["user"])
                print("   Category:", x["category"])
                print("   Notes:", x["notes"])
                found = True

        if not found:
            print("No matching entry found.")

    def reveal(self):
        i = self.select()
        if i is None:
            return

        entered = getpass.getpass("Re-enter master password: ")
        if hash_master(entered) != self.master_hash:
            print("Incorrect master password.")
            return

        x = self.data[i]
        print("Site:", x["site"])
        print("Username:", x["user"])
        print("Password:", x["password"])

    def update(self):
        i = self.select()
        if i is None:
            return

        x = self.data[i]
        print("Press Enter to keep the current value.")

        site = input("Website/App [",x['site'],"]: ")
        user = input("Username/Email [",x['user'],"]: ")
        cat = input("Category [",x['category'],"]: ")
        note = input("Notes [",x['notes'],"]: ")

        if site:
            x["site"] = site
        if user:
            x["user"] = user
        if cat:
            x["category"] = cat
        if note:
            x["notes"] = note

        if input("Change password? (y/n): ").strip().lower() == "y":
            password = getpass.getpass("New password: ")
            if password:
                if was_used(password):
                    print("Warning: you have used this password before.")
                x["password"] = password
                add_to_history(password)
                show_strength(password)

        x["modified"] = now()
        self.unsaved = True
        print("Entry updated.")

    def delete(self):
        i = self.select()
        if i is None:
            return
        
        choice = input("Delete this entry? (y/n): ").strip().lower()
        if choice == "y":
            self.data.pop(i)
            self.unsaved = True
            print("Entry deleted.")
        else:
            print("Deletion cancelled.")