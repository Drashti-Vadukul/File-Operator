# 📔 File Operator : Personal Journal Manager

## 👩‍💻 Author

**Drashti Vadukul**

- BCA Student
- Learning AI, ML & Data Science
- Interested in Python, Data Analytics & Web Development

---

## 📌 Project Overview

The **Personal Journal Manager** is a simple and beginner-friendly **Python-based Personal Journal Manager** designed to store and manage personal journal entries using **File Handling**.

This project provides a menu-driven interface that allows users to:

1. Add a new journal entry
2. View previously saved entries
3. Search for specific entries using keywords or dates
4. Delete all stored entries
5. Exit the application

The main purpose of this project is to understand how Python can be used to work with files and build a practical command-line application.

---

## 🎯 Project Objectives

The main objectives of this project are:

- To understand how file handling works in Python.
- To store data permanently inside a text file.
- To read previously stored data from a file.
- To add new information without deleting existing information.
- To search stored information using keywords or dates.
- To delete stored information when required.
- To understand how classes and methods can organize a Python program.
- To handle possible file-related errors using exception handling.
- To create a simple real-world application using Python.

---

## 🚀 Features

### 1. ➕ Add a New Entry

The user can enter a personal journal entry through the console.

The program automatically records the current date and time along with the journal entry.

#### Example

```text
Enter Your Journal Entry :
Today is a sweet day

Entry Added Successfully!
```

The entry is stored permanently inside the `journal.txt` file.

### 2. 📖 View All Entries

The user can view all previously stored journal entries.

Each entry contains:

- Date
- Time
- Journal text

#### Example

```text
Output (If the file exists):

Your Journal Entries:

--------------------------------------------------

[2026-10-02 18:00:02.781395]

Vadukul Drashti

[2026-10-02 18:00:13.722077]

I'm currently working on project

[2026-10-02 18:00:53.674354]

Today is a sweet day
```

This option helps the user review all the journal entries saved in the file.

### 3. 🔍 Search for an Entry

The search feature allows the user to find a particular journal entry.

The user can enter:

- A keyword
- A date
- Complete or partial text

The program checks the stored entries and displays the matching entry.

#### Example

```text
Enter a keyword or date to Search : hello

Matching Entry:
hello
```

Another example:

```text
Enter a keyword or date to Search : Vadukul Drashti

Matching Entry:
Vadukul Drashti
```

The search is performed without requiring an exact case match.

For example, searching for:

```text
vadukul
```

can also find:

```text
Vadukul Drashti
```

If no matching entry is found, the program displays:

```text
No Entries were found for the keyword: Drashti Vadukul.
```

### 4. 🗑️ Delete All Entries

The delete option allows the user to remove all journal entries from the file.

Before deleting the data, the program asks the user for confirmation.

#### Example

```text
Are you sure you want to delete all entries (yes/no): yes

All Journal Entries have been deleted successfully.
```

If the user selects `no`, the entries remain safe.

This confirmation step helps prevent accidental deletion of journal data.

### 5. 🚪 Exit

The Exit option terminates the program.

#### Example

```text
Thank you for using Personal Journal Manager. Goodbye!
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **File Handling** | Store and manage journal entries |
| **datetime** | Store date and time |
| **Exception Handling** | Handle file-related errors |
| **OOP** | Organize the program using classes and methods |
| **String Methods** | Search and compare journal entries |
| **Conditional Statements** | Control program decisions |
| **Loops** | Repeatedly display the menu |

---

## 🧠 Python Concepts Used

### 1. Classes and Objects

The project uses a class to organize the journal management functionality.

```python
class JournalManager:
```

The class contains different methods for performing operations such as:

```python
add_entry()
view_entries()
search_entry()
delete_entries()
```

This keeps the program organized and makes each operation easier to manage.

### 2. Constructor

The `__init__()` method is used to initialize the journal file.

#### Example

```python
def __init__(self):
    self.filename = "journal.txt"
```

The filename is stored as an object attribute so that different methods can use the same file.

### 3. File Handling

File handling is one of the main concepts used in this project.

The program works with a text file named:

```text
journal.txt
```

Different file modes are used for different operations.

#### Read Mode

```python
open(self.filename, "r")
```

Used to read existing journal entries.

#### Append Mode

```python
open(self.filename, "a")
```

Used to add new entries without removing old entries.

#### Write Mode

```python
open(self.filename, "w")
```

Can be used when the file needs to be overwritten or cleared.

#### Create Mode

```python
open(self.filename, "x")
```

Used to create the journal file if it does not already exist.

### 4. ⏰ Date and Time

The project uses Python's `datetime` module to record when an entry was created.

#### Example

```python
import datetime
```

A timestamp is stored with every journal entry.

#### Example

```text
[2026-10-02 18:05:07.875918]
```

This makes it easier to identify when each journal entry was added.

### 5. ⚠️ Exception Handling

The program uses exception handling to prevent the application from crashing when a file-related problem occurs.

#### Example

```python
try:
    ...
except FileExistsError:
    ...
```

This is useful when the program tries to create a file that already exists.

Exception handling makes the application more reliable and user-friendly.

### 6. 🔎 Search Logic

The search functionality checks whether the entered keyword exists inside a journal entry.

The search can be performed using:

```python
keyword.lower()
```

and:

```python
entry.lower()
```

Converting both values to lowercase allows the program to perform a case-insensitive search.

For example:

```text
Search: vadukul
```

can match:

```text
Vadukul Drashti
```

This makes the search feature easier for the user.

---

## 📋 Menu-Driven Interface

The project uses a menu-driven system so that the user can continuously perform different operations.

The main menu is:

```text
Welcome to Personal Journal Manager!

Please Select an Option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

The program repeatedly displays this menu until the user selects option `5`.

---

## 🔄 Program Flow

The overall working of the application is:

```text
Start
  │
  ▼
Create / Open Journal File
  │
  ▼
Display Main Menu
  │
  ├── 1 → Add New Entry
  │       │
  │       ▼
  │   Save Entry + Date/Time
  │
  ├── 2 → View All Entries
  │       │
  │       ▼
  │   Read journal.txt
  │
  ├── 3 → Search Entry
  │       │
  │       ▼
  │   Enter Keyword / Date
  │       │
  │       ▼
  │   Display Matching Entry
  │
  ├── 4 → Delete All Entries
  │       │
  │       ▼
  │   Ask Confirmation
  │       │
  │       ▼
  │   Delete Stored Entries
  │
  └── 5 → Exit
          │
          ▼
         End
```

---

## 📂 Project Structure

```text
Personal-Journal-Manager/
│
├── File_Operator.py
├── journal.txt
├── File_Operator.png
└── README.md
```

### File Description

| File | Description |
|---|---|
| `File_Operator.py` | Main Python program |
| `journal.txt` | Stores journal entries |
| `File_Operator.png` | Project output screenshots |
| `README.md` | Project documentation |

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

Clone the project from GitHub or download the repository.

### Step 2: Open the Project

Open the project folder in **Visual Studio Code**.

### Step 3: Open Terminal

Open the VS Code terminal.

### Step 4: Run the Program

Use:

```bash
python File_Operator.py
```

The program will display the main menu.

---

## 💻 Sample Output

### Main Menu

```text
Welcome to Personal Journal Manager!

Please Select an Option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

### Adding an Entry

#### User Input

```text
1
```

```text
Enter Your Journal Entry :

Vadukul Drashti

Entry Added Successfully!
```

### Viewing Entries

#### User Input

```text
2
```

#### Output

```text
Your Journal Entries:

--------------------------------------------------

[2026-10-02 18:05:07.875918]

Vadukul Drashti

[2026-10-02 18:05:36.633510]

I do not have a idea what do i do...
```

### Searching an Entry

#### User Input

```text
3
```

```text
Enter a keyword or date to Search : Vadukul

Matching Entry:

Vadukul Drashti
```

### No Match Found

```text
No Entries were found for the keyword: Drashti Vadukul.
```

### Deleting Entries

#### User Input

```text
4
```

```text
Are you sure you want to delete all entries (yes/no): yes

All Journal Entries have been deleted successfully.
```

### Exit

#### User Input

```text
5
```

```text
Thank you for using Personal Journal Manager. Goodbye!
```

---

---

## ❌ Invalid Input Handling

The program also handles invalid menu choices.

For example, if the user enters:

```text
6
```

the program displays:

```text
Invalid option. Please select a valid option from the menu.
```

This prevents the program from performing an unknown operation.

---

## 📚 Learning Outcomes

After completing this project, I gained practical understanding of:

- Python file handling
- Creating and managing text files
- Reading data from files
- Writing data to files
- Appending data to existing files
- Creating files using Python
- Exception handling
- Working with `datetime`
- Object-oriented programming
- Creating classes
- Creating methods
- Using constructors
- String manipulation
- Case-insensitive searching
- Conditional statements
- Loops
- User input handling
- Menu-driven applications
- Building a practical Python project

---

## 🎓 Project Purpose

This project was created as a practical Python project to apply fundamental programming concepts in a real-world style application.

Instead of storing journal entries temporarily in variables, the project uses file handling so that the data can remain stored even after the program is closed.

This project helped me understand how basic Python concepts can be combined to create a useful application.

---

## 🔮 Future Improvements

The project can be improved further by adding:

- Edit an existing journal entry
- Delete a specific journal entry
- Search entries by a specific date
- Display entries in a better formatted way
- Add categories or tags to journal entries
- Add password protection
- Store data using JSON or a database
- Add a graphical user interface using Tkinter
- Add sorting options
- Add backup and restore functionality

---

## ⭐ Conclusion

The **Personal Journal Manager** is a beginner-friendly Python application that demonstrates how file handling, object-oriented programming, exception handling, date and time functionality, searching, and menu-driven programming can work together in a single project.

This project provides a strong practical foundation for developing more advanced Python applications in the future.
