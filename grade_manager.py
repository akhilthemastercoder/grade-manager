#!/usr/bin/env python3
"""
Grade Manager - A simple student grade tracking system
Author: Akhil
Version: 1.0.0
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional, Union

class GradeManager:
    """A comprehensive grade management system with error handling"""
    
    def __init__(self, data_file: str = "grades.json"):
        """Initialize the GradeManager with a data file"""
        self.data_file = data_file
        self.students: Dict[str, List[Dict]] = {}
        self.load_data()
    
    def load_data(self) -> None:
        """Load student data from file with comprehensive error handling"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.students = json.load(f)
                print(f"✅ Loaded data for {len(self.students)} students")
            else:
                print("📝 No existing data found. Starting fresh!")
                self.students = {}
        except json.JSONDecodeError:
            print("❌ Error: Invalid JSON format in data file!")
            self._backup_corrupted_file()
            self.students = {}
        except PermissionError:
            print("❌ Error: Permission denied reading data file")
            self.students = {}
        except Exception as e:
            print(f"❌ Unexpected error loading data: {e}")
            self.students = {}
    
    def _backup_corrupted_file(self) -> None:
        """Create backup of corrupted file"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_name = f"backup_{timestamp}.json"
            os.rename(self.data_file, backup_name)
            print(f"💾 Corrupted file backed up as: {backup_name}")
        except Exception as e:
            print(f"❌ Could not create backup: {e}")
    
    def save_data(self) -> bool:
        """Save student data to file with error handling"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.students, f, indent=2, ensure_ascii=False)
            return True
        except PermissionError:
            print("❌ Error: Permission denied. Cannot write to file.")
            return False
        except OSError as e:
            print(f"❌ Error saving data: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error saving data: {e}")
            return False
    
    def add_student(self, name: str) -> bool:
        """Add a new student with validation"""
        try:
            if not name or not isinstance(name, str):
                raise ValueError("Name must be a non-empty string")
            
            clean_name = name.strip().title()
            if not clean_name:
                raise ValueError("Name cannot be empty after cleaning")
            
            if clean_name in self.students:
                raise ValueError(f"Student '{clean_name}' already exists!")
            
            self.students[clean_name] = []
            print(f"✅ Added student: {clean_name}")
            return self.save_data()
            
        except ValueError as e:
            print(f"❌ Validation Error: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error adding student: {e}")
            return False
    
    def add_grade(self, student_name: str, subject: str, grade: Union[int, float]) -> bool:
        """Add a grade for a student with comprehensive validation"""
        try:
            if student_name not in self.students:
                raise ValueError(f"Student '{student_name}' not found!")
            
            if not subject or not isinstance(subject, str):
                raise ValueError("Subject must be a non-empty string")
            
            clean_subject = subject.strip().title()
            if not clean_subject:
                raise ValueError("Subject cannot be empty after cleaning")
            
            if not isinstance(grade, (int, float)):
                raise TypeError("Grade must be a number")
            
            if not (0 <= grade <= 100):
                raise ValueError("Grade must be between 0 and 100")
            
            grade_entry = {
                "subject": clean_subject,
                "grade": float(grade),
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            self.students[student_name].append(grade_entry)
            print(f"✅ Added grade: {student_name} - {clean_subject}: {grade}")
            return self.save_data()
            
        except (ValueError, TypeError) as e:
            print(f"❌ Error: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error adding grade: {e}")
            return False
    
    def get_student_average(self, student_name: str) -> Optional[float]:
        """Calculate student's average grade"""
        try:
            if student_name not in self.students:
                raise ValueError(f"Student '{student_name}' not found!")
            
            grades = self.students[student_name]
            if not grades:
                raise ValueError(f"No grades found for {student_name}")
            
            total = sum(grade["grade"] for grade in grades)
            average = total / len(grades)
            
            print(f"📊 {student_name}'s average: {average:.2f}")
            return average
            
        except ValueError as e:
            print(f"❌ Error: {e}")
            return None
        except Exception as e:
            print(f"❌ Unexpected error calculating average: {e}")
            return None
    
    def show_student_grades(self, student_name: str) -> None:
        """Display all grades for a student"""
        try:
            if student_name not in self.students:
                raise ValueError(f"Student '{student_name}' not found!")
            
            grades = self.students[student_name]
            if not grades:
                print(f"📚 No grades found for {student_name}")
                return
            
            print(f"\n📚 Grades for {student_name}:")
            print("-" * 50)
            for i, grade_info in enumerate(grades, 1):
                print(f"{i:2d}. {grade_info['subject']:15} {grade_info['grade']:5.1f} ({grade_info['date']})")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error showing grades: {e}")
    
    def show_all_students(self) -> None:
        """Display all students and their statistics"""
        try:
            if not self.students:
                print("📝 No students found!")
                return
            
            print("\n👥 All Students:")
            print("=" * 70)
            print(f"{'Name':<20} {'Grades':<8} {'Average':<10} {'Status'}")
            print("-" * 70)
            
            for name, grades in self.students.items():
                grade_count = len(grades)
                if grade_count > 0:
                    average = sum(g["grade"] for g in grades) / grade_count
                    status = "🟢" if average >= 80 else "🟡" if average >= 60 else "🔴"
                    print(f"{name:<20} {grade_count:<8} {average:<10.2f} {status}")
                else:
                    print(f"{name:<20} {grade_count:<8} {'N/A':<10} ⚪")
            
        except Exception as e:
            print(f"❌ Unexpected error showing students: {e}")
    
    def delete_student(self, student_name: str) -> bool:
        """Delete a student with confirmation"""
        try:
            if student_name not in self.students:
                raise ValueError(f"Student '{student_name}' not found!")
            
            grade_count = len(self.students[student_name])
            print(f"\n⚠️  Are you sure you want to delete {student_name}?")
            print(f"   This will remove {grade_count} grades!")
            
            confirm = input("Type 'yes' to confirm: ").strip().lower()
            if confirm == 'yes':
                del self.students[student_name]
                print(f"✅ Deleted student: {student_name}")
                return self.save_data()
            else:
                print("❌ Deletion cancelled")
                return False
                
        except ValueError as e:
            print(f"❌ Error: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error deleting student: {e}")
            return False
    
    def export_grades(self, filename: Optional[str] = None) -> bool:
        """Export grades to a text file"""
        try:
            if not filename:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"grades_export_{timestamp}.txt"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("STUDENT GRADE REPORT\n")
                f.write("=" * 50 + "\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                for name, grades in self.students.items():
                    f.write(f"Student: {name}\n")
                    f.write("-" * 30 + "\n")
                    
                    if grades:
                        for grade_info in grades:
                            f.write(f"  {grade_info['subject']}: {grade_info['grade']} ({grade_info['date']})\n")
                        
                        average = sum(g["grade"] for g in grades) / len(grades)
                        f.write(f"  Average: {average:.2f}\n")
                    else:
                        f.write("  No grades\n")
                    
                    f.write("\n")
            
            print(f"📄 Grades exported to: {filename}")
            return True
            
        except PermissionError:
            print("❌ Error: Permission denied. Cannot write to file.")
            return False
        except Exception as e:
            print(f"❌ Unexpected error exporting grades: {e}")
            return False
    
    def get_statistics(self) -> None:
        """Display overall statistics"""
        try:
            if not self.students:
                print("📝 No students found!")
                return
            
            total_students = len(self.students)
            total_grades = sum(len(grades) for grades in self.students.values())
            
            if total_grades == 0:
                print("📊 No grades found!")
                return
            
            all_grades = []
            for grades in self.students.values():
                all_grades.extend([g["grade"] for g in grades])
            
            average_all = sum(all_grades) / len(all_grades)
            highest = max(all_grades)
            lowest = min(all_grades)
            
            print(f"\n📊 Overall Statistics:")
            print("-" * 30)
            print(f"Total Students: {total_students}")
            print(f"Total Grades: {total_grades}")
            print(f"Overall Average: {average_all:.2f}")
            print(f"Highest Grade: {highest}")
            print(f"Lowest Grade: {lowest}")
            
        except Exception as e:
            print(f"❌ Unexpected error getting statistics: {e}")

def display_menu() -> None:
    """Display the main menu"""
    print("\n" + "="*60)
    print("🎓 STUDENT GRADE MANAGER v1.0.0")
    print("="*60)
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View Student Grades")
    print("4. Calculate Average")
    print("5. Show All Students")
    print("6. Delete Student")
    print("7. Export Grades")
    print("8. Show Statistics")
    print("9. Exit")
    print("-"*60)

def get_menu_choice() -> str:
    """Get and validate menu choice"""
    while True:
        choice = input("Choose an option (1-9): ").strip()
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return choice
        print("❌ Invalid choice. Please enter 1-9.")

def main() -> None:
    """Main program loop"""
    manager = GradeManager()
    
    print("🎓 Welcome to Grade Manager!")
    print("📝 Managing student grades with style!")
    
    while True:
        display_menu()
        choice = get_menu_choice()
        
        try:
            if choice == '1':
                name = input("Enter student name: ").strip()
                manager.add_student(name)
            
            elif choice == '2':
                student_name = input("Enter student name: ").strip()
                subject = input("Enter subject: ").strip()
                grade_input = input("Enter grade (0-100): ").strip()
                
                try:
                    grade = float(grade_input)
                    manager.add_grade(student_name, subject, grade)
                except ValueError:
                    print("❌ Error: Grade must be a number!")
            
            elif choice == '3':
                student_name = input("Enter student name: ").strip()
                manager.show_student_grades(student_name)
            
            elif choice == '4':
                student_name = input("Enter student name: ").strip()
                manager.get_student_average(student_name)
            
            elif choice == '5':
                manager.show_all_students()
            
            elif choice == '6':
                student_name = input("Enter student name to delete: ").strip()
                manager.delete_student(student_name)
            
            elif choice == '7':
                filename = input("Enter filename (or press Enter for auto): ").strip()
                if not filename:
                    filename = None
                manager.export_grades(filename)
            
            elif choice == '8':
                manager.get_statistics()
            
            elif choice == '9':
                print("👋 Thank you for using Grade Manager!")
                break
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
