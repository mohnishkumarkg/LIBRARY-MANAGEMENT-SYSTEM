# 📚 Library Management System (Python)

A robust, object-oriented **Library Management System** built in Python.  
This project demonstrates clean class design, exception handling, and real-world workflows for managing books and students.

---

## 🚀 Features
- **Book Management**: Unique IDs, duplicate prevention, availability tracking
- **Student Management**: Registration, borrowed books list, history
- **Library Operations**:
  - Issue and return books with due dates
  - Generate reports on issued and overdue books
  - Track borrowing history
- **Exception Handling**: Custom error classes for predictable system behavior

---

## 🛠️ Tech Highlights
- Python OOP principles (`Book`, `Student`, `Library` classes)
- Exception handling (`BookNotFoundError`, `BookAlreadyExists`, etc.)
- Date management with `datetime` and `timedelta`
- Enhanced console UX with `colorama`

---
📂 Project Structure
LibraryManagementSystem/
│
├── README.md
├── LICENSE
├── requirements.txt
├── main.py
│
├── library/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── book.py
│   ├── student.py
│   ├── library.py
│   └── demo.py
│
├── data/
│   ├── books.json
│   ├── students.json
│   └── transactions.json
│
├── reports/
│   ├── issued_books.txt
│   ├── overdue_books.txt
│   └── borrowing_history.txt
│
├── tests/
│   ├── test_book.py
│   ├── test_student.py
│   ├── test_library.py
│   └── test_exceptions.py
│
└── docs/
    ├── architecture.md
    ├── usage.md
    └── phase2_plan.md

