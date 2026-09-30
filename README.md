# Password Generator & Vault

A modular Python CLI project for the VITyarthi Build Your Own Project evaluation.

## Features

- Random password generation
- Password strength checking
- Website/App + Username/Email + Password vault
- Category and notes
- Add, view, search, update and delete operations
- Password history using SHA-256 hashes instead of storing historical passwords
- Local persistence
- Input validation
- Basic automated tests

## Project Structure

```text
password-vault/
├── main.py
├── ui.py
├── generator.py
├── security.py
├── history.py
├── vault.py
├── tests.py
├── requirements.txt
├── statement.md
├── README.md
└── vault.dat
```

## Requirements

- Python 3.10 or later
- No external package is required for this academic version.

## Run

```bash
python main.py
```

## Test

```bash
python tests.py
```

## Functional Modules

### 1. Password Generator
Creates a random password containing lowercase letters, uppercase letters,
digits and special characters.

### 2. Security Analyzer
Checks password length, character variety and repeated-character usage.

### 3. Password History
Stores SHA-256 hashes and timestamps instead of the original historical
passwords.

### 4. Password Vault
Stores Website/App, Username/Email, Password, Category, Notes, Created and
Modified information.

### 5. Vault Operations
Provides add, view, search, update and delete functionality.

## Security Note

This is an academic project. The current Version 1 demonstrates password
history hashing and basic access control. The next security upgrade should use
a modern password-derived key and authenticated encryption before the vault is
used for real credentials.

## Git

Recommended workflow:

```bash
git init
git add .
git commit -m "Initial Password Vault project"
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main
```
