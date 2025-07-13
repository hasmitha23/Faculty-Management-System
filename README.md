# Faculty Information System (Console-Based)

A secure and user-friendly console-based Python application designed to manage faculty records, including names, departments, and course assignments. This project is ideal for beginners learning CRUD operations, file handling, and authentication in Python.


## 💡 Features

Admin Login Protection
  - Only authorized admin can access the system
  - Password input is hidden using `getpass`

Faculty Data Management
  - Add new faculty records (ID, name, department, courses)
  - View all faculty details
  - Update existing faculty information
  - Delete faculty records by ID

Reports and Export
  - Generate a readable `.txt` report of faculty data
  - Export a well-formatted `.pdf` report using `reportlab`

Persistent Storage
  - Data is saved in `faculty_data.json` and automatically loaded when the program starts


## 🛠 Technologies Used

- Python 3.x
- `getpass` for secure login
- `json` for persistent data storage
- `reportlab` for PDF report generation




