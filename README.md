# 🎓 Grade Manager

A comprehensive Python application for managing student grades with robust error handling and data persistence.

## ✨ Features

- **Student Management**: Add, view, and delete students
- **Grade Tracking**: Add grades for different subjects with validation
- **Statistics**: Calculate averages and view overall statistics
- **Data Persistence**: Automatic saving and loading of data
- **Error Handling**: Comprehensive error handling for robust operation
- **Export Functionality**: Export grades to text files
- **Interactive Menu**: User-friendly command-line interface

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/grade-manager.git
   cd grade-manager
   ```

2. **Run the application:**
   ```bash
   python grade_manager.py
   ```

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## 🎯 Usage

### Main Menu Options

1. **Add Student** - Add a new student to the system
2. **Add Grade** - Add a grade for a specific student and subject
3. **View Student Grades** - Display all grades for a specific student
4. **Calculate Average** - Calculate and display student's average grade
5. **Show All Students** - Display all students with their statistics
6. **Delete Student** - Remove a student and all their grades
7. **Export Grades** - Export all grades to a text file
8. **Show Statistics** - Display overall statistics
9. **Exit** - Quit the application

### Example Usage

```python
# The application will guide you through each step
# Example workflow:
1. Add Student: "Alice Johnson"
2. Add Grade: Alice Johnson, Math, 85
3. Add Grade: Alice Johnson, Science, 92
4. View Student Grades: Alice Johnson
5. Calculate Average: Alice Johnson
```

## 📁 Project Structure

```
grade-manager/
├── grade_manager.py      # Main application file
├── README.md            # This file
├── requirements.txt     # Dependencies (none for this project)
├── grades.json         # Data file (created automatically)
└── .gitignore          # Git ignore file
```

## 🔧 Technical Details

### Error Handling

The application includes comprehensive error handling for:

- **File Operations**: Missing files, permission errors, corrupted data
- **Data Validation**: Invalid inputs, type errors, range validation
- **User Input**: Invalid menu choices, malformed data
- **System Errors**: Unexpected exceptions with graceful recovery

### Data Storage

- Uses JSON format for data persistence
- Automatic backup of corrupted files
- UTF-8 encoding for international character support

### Code Quality

- Type hints for better code documentation
- Comprehensive docstrings
- Modular design with clear separation of concerns
- Consistent error handling patterns

## 🧪 Testing

The application can be tested with various scenarios:

1. **Normal Operation**: Add students and grades
2. **Error Handling**: Try invalid inputs, missing files
3. **Data Persistence**: Restart application and verify data is saved
4. **Edge Cases**: Empty names, invalid grades, non-existent students

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Akhil**
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

## 🎉 Acknowledgments

- Built with Python standard library
- Inspired by the need for simple grade management
- Thanks to the Python community for excellent documentation

## 📊 Screenshots

```
🎓 STUDENT GRADE MANAGER v1.0.0
============================================================
1. Add Student
2. Add Grade
3. View Student Grades
4. Calculate Average
5. Show All Students
6. Delete Student
7. Export Grades
8. Show Statistics
9. Exit
------------------------------------------------------------
Choose an option (1-9): 
```

---

**Made with ❤️ and Python**
