import getpass
import json
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# 🔐 Admin Login Credentials
admin_id = "hasmi8866"
admin_password = "hasmi@123"

print("=" * 50)
print("🔐 Admin Login Required".center(50))
print("=" * 50)

entered_id = input("Enter Admin ID: ").strip()
entered_pass = getpass.getpass("Enter Password: ").strip()

if entered_id != admin_id or entered_pass != admin_password:
    print("❌ Access Denied! Invalid credentials.")
    exit()
else:
    print("✅ Login Successful! Welcome, Hasmitha(Admin).")

# 📁 File to store data
DATA_FILE = "faculty_data.json"

# 🧠 Faculty Database
faculty_db = {}

# 🧩 Load existing data
def load_data():
    global faculty_db
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            faculty_db = json.load(f)

# 💾 Save data
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(faculty_db, f, indent=4)

# 📜 Menu
def show_menu():
    print("\n🎓 Faculty Information System Menu")
    print("1. ➕ Add Faculty")
    print("2. 📋 View All Faculty")
    print("3. ✏️ Update Faculty")
    print("4. ❌ Delete Faculty")
    print("5. 🖨 Generate Text Report")
    print("6. 📄 Export Report as PDF")
    print("7. 🚪 Exit")

# 🚀 Load existing data on startup
load_data()

# 🌟 Main Loop
print("=" * 50)
print("📚 Welcome to Faculty Information System 📚".center(50))
print("=" * 50)

while True:
    show_menu()
    choice = input("\nEnter your choice (1-7): ").strip()

    if choice == '1':
        print("\n➕ Add Faculty")
        faculty_id = input("Enter Faculty ID (e.g., F101): ").strip()
        if faculty_id in faculty_db:
            print("⚠️ Faculty ID already exists.")
        else:
            name = input("Enter Faculty Name: ").strip().title()
            department = input("Enter Department: ").strip().title()
            courses = input("Enter Courses (comma-separated): ").strip().title().split(',')
            courses = [course.strip() for course in courses]
            faculty_db[faculty_id] = {
                "name": name,
                "department": department,
                "courses": courses
            }
            save_data()
            print(f"✅ Faculty {name} added successfully!")

    elif choice == '2':
        print("\n📋 Faculty List")
        if not faculty_db:
            print("😶 No faculty records found.")
        else:
            print("-" * 70)
            print(f"{'ID':<10} {'Name':<20} {'Department':<20} {'Courses'}")
            print("-" * 70)
            for fid, data in faculty_db.items():
                course_list = ', '.join(data['courses'])
                print(f"{fid:<10} {data['name']:<20} {data['department']:<20} {course_list}")
            print("-" * 70)
            print(f"👥 Total Faculty: {len(faculty_db)}")

    elif choice == '3':
        print("\n✏️ Update Faculty")
        fid = input("Enter Faculty ID to update: ").strip()
        if fid not in faculty_db:
            print("❌ Faculty ID not found.")
        else:
            print("What would you like to update?")
            print("1. Name")
            print("2. Department")
            print("3. Courses")
            print("4. All")
            update_choice = input("Enter choice (1-4): ").strip()

            if update_choice == '1':
                new_name = input("Enter new name: ").strip().title()
                faculty_db[fid]['name'] = new_name
            elif update_choice == '2':
                new_dept = input("Enter new department: ").strip().title()
                faculty_db[fid]['department'] = new_dept
            elif update_choice == '3':
                new_courses = input("Enter new courses (comma-separated): ").strip().title().split(',')
                faculty_db[fid]['courses'] = [c.strip() for c in new_courses]
            elif update_choice == '4':
                new_name = input("Enter new name: ").strip().title()
                new_dept = input("Enter new department: ").strip().title()
                new_courses = input("Enter new courses (comma-separated): ").strip().title().split(',')
                faculty_db[fid] = {
                    "name": new_name,
                    "department": new_dept,
                    "courses": [c.strip() for c in new_courses]
                }
            else:
                print("⚠️ Invalid update option.")
                continue
            save_data()
            print("✅ Faculty updated.")

    elif choice == '4':
        print("\n❌ Delete Faculty")
        fid = input("Enter Faculty ID to delete: ").strip()
        if fid in faculty_db:
            confirm = input(f"Are you sure you want to delete {faculty_db[fid]['name']}? (yes/no): ").lower()
            if confirm == 'yes':
                del faculty_db[fid]
                save_data()
                print("✅ Faculty deleted.")
            else:
                print("❎ Deletion cancelled.")
        else:
            print("⚠️ Faculty ID not found.")

    elif choice == '5':
        print("\n🖨 Generating Text Report...")
        report_file = "faculty_report.txt"
        with open(report_file, "w", encoding="utf-8") as f:
            f.write("📚 Faculty Report\n")
            f.write("=" * 70 + "\n")
            f.write(f"{'ID':<10} {'Name':<20} {'Department':<20} {'Courses'}\n")
            f.write("-" * 70 + "\n")
            for fid, data in faculty_db.items():
                courses = ", ".join(data['courses'])
                f.write(f"{fid:<10} {data['name']:<20} {data['department']:<20} {courses}\n")
            f.write("-" * 70 + "\n")
            f.write(f"Total Faculty: {len(faculty_db)}\n")
        print(f"✅ Text report saved as '{report_file}'.")

    elif choice == '6':
        print("\n📄 Generating PDF Report...")
        pdf_file = "faculty_report.pdf"
        c = canvas.Canvas(pdf_file, pagesize=A4)
        width, height = A4

        c.setFont("Helvetica-Bold", 16)
        c.drawString(200, height - 50, "Faculty Report")
        c.setFont("Helvetica", 12)

        y = height - 100
        c.drawString(40, y, f"{'ID':<10} {'Name':<20} {'Department':<20} {'Courses'}")
        y -= 20
        c.line(40, y, width - 40, y)
        y -= 20

        for fid, data in faculty_db.items():
            courses = ", ".join(data['courses'])
            line = f"{fid:<10} {data['name']:<20} {data['department']:<20} {courses}"
            if y < 80:
                c.showPage()
                y = height - 100
            c.drawString(40, y, line)
            y -= 20

        c.drawString(40, y - 10, "-" * 90)
        y -= 30
        c.drawString(40, y, f"Total Faculty: {len(faculty_db)}")
        c.save()

        print(f"✅ PDF report saved as '{pdf_file}'!")

    elif choice == '7':
        print("\n👋 Exiting Faculty Information System. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice. Please enter a number from 1 to 7.")
