# VITyarthi Documentation

## 1. Objectives

- Apply Python programming concepts to a real-world problem.
- Demonstrate modular programming and functions/classes.
- Use conditional logic, loops, strings, lists, dictionaries and file handling.
- Demonstrate hashing and basic security concepts.
- Implement CRUD operations.
- Validate input and handle errors.
- Maintain a GitHub-ready project structure.

## 2. Functional Requirements

| ID | Requirement |
|---|---|
| FR1 | Generate a random password |
| FR2 | Check password strength |
| FR3 | Add a vault entry |
| FR4 | View vault entries |
| FR5 | Search vault entries |
| FR6 | Update vault entries |
| FR7 | Delete vault entries |
| FR8 | Maintain password history hashes |
| FR9 | Save vault data locally |

## 3. Non-Functional Requirements

| Requirement | Project implementation |
|---|---|
| Security | Password history uses SHA-256 hashes; password input uses hidden terminal input |
| Usability | Menu-driven CLI and clear prompts |
| Reliability | File errors and invalid input are handled |
| Maintainability | Functions/classes separated into modules |
| Performance | In-memory list operations are suitable for a small student vault |
| Resource efficiency | Uses lightweight standard-library components |

## 4. System Architecture

```text
                 +------------------+
                 |     main.py      |
                 |  Control Layer   |
                 +--------+---------+
                          |
        +-----------------+------------------+
        |                 |                  |
        v                 v                  v
     ui.py          generator.py        security.py
        |                 |                  |
        +-----------------+------------------+
                          |
                          v
                     vault.py
                          |
             +------------+------------+
             |                         |
             v                         v
        history.py                  vault.dat
```

## 5. Workflow

```text
Start
  |
  v
Display Header
  |
  v
Enter Master Password
  |
  v
Main Menu
  |
  +--> Generate Password --> Strength Check
  |
  +--> Add Entry ----------> Validate --> Store
  |
  +--> View/Search
  |
  +--> Update Entry
  |
  +--> Delete Entry
  |
  +--> Password History
  |
  +--> Save Vault
  |
  v
Exit
```

## 6. Use Case Diagram

```text
                 +----------------------+
                 |    Password Vault    |
                 +----------------------+
 User ---------->| Generate Password    |
 User ---------->| Check Strength      |
 User ---------->| Add Credential      |
 User ---------->| View Credentials    |
 User ---------->| Search Credentials  |
 User ---------->| Update Credential   |
 User ---------->| Delete Credential   |
 User ---------->| View Password Hash  |
 User ---------->| Save Vault          |
                 +----------------------+
```

## 7. Class / Component Diagram

```text
+------------------+
|      Vault       |
+------------------+
| data             |
| master           |
+------------------+
| login()          |
| add()            |
| view()           |
| search()         |
| update()         |
| delete()         |
| save()           |
+------------------+

Vault uses:
- generator.gen()
- security.chk()
- history.addh()
- ui functions
```

## 8. Sequence Diagram

```text
User -> main.py: Select Add Entry
main.py -> vault.py: add()
vault.py -> User: Request website/user
vault.py -> generator.py: gen()
generator.py -> vault.py: Password
vault.py -> security.py: chk(password)
security.py -> vault.py: Strength
vault.py -> history.py: addh(password)
history.py -> vault.py: SHA-256 hash
vault.py -> main.py: Entry added
main.py -> User: Confirmation
```

## 9. Storage Design

Each vault record contains:

```text
site
user
password
category
notes
created
modified
```

Password history contains:

```text
hash
time
```

## 10. Testing

Test cases include:

| Test | Expected Result |
|---|---|
| Generate password | 14-character mixed password |
| Weak password | Weak classification |
| Strong password | Moderate/Strong classification |
| Empty website | Entry rejected |
| Empty username | Entry rejected |
| Search existing site | Matching entry displayed |
| Search unknown site | No match message |
| Invalid menu choice | Error message |
| Invalid entry number | Error message |
| Save vault | vault.dat created/updated |

## 11. Future Enhancements

- Replace plaintext vault storage with authenticated encryption.
- Use a password-derived encryption key.
- Add automatic lock timeout.
- Add password expiry reminders.
- Add categories and sorting filters.
- Add import/export with secure encryption.
- Add a graphical user interface.
