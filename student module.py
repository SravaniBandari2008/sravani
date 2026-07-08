# ==========================================
# CareerPilot - Student Profile Module
# Sprint 1
# ==========================================

# List to store all student profiles
students = []


def create_profile():
    """
    Create a new student profile. 
    """

    print("\n===== Create Student Profile =====")

    name = input("Enter Student Name   : ").strip()
    roll_no = input("Enter Roll Number    : ").strip()
    branch = input("Enter Branch         : ").strip()
    year = input("Enter Year           : ").strip()
    career_goal = input("Enter Career Goal   : ").strip()

    # Basic Validation
    if name == "":
        print("\nStudent name cannot be empty!")
        return

    # Create one student profile
    student = {
        "name": name,
        "roll_no": roll_no,
        "branch": branch,
        "year": year,
        "career_goal": career_goal
    }

    # Store inside the list
    students.append(student)

    print("\n✅ Student Profile Created Successfully!\n")


def view_profiles():
    """
    Display all student profiles.
    """

    print("\n===== Student Profiles =====")

    if len(students) == 0:
        print("No student profiles found.\n")
        return

    for index, student in enumerate(students, start=1):

        print(f"\nStudent {index}")

        print(f"Name          : {student['name']}")
        print(f"Roll Number   : {student['roll_no']}")
        print(f"Branch        : {student['branch']}")
        print(f"Year          : {student['year']}")
        print(f"Career Goal   : {student['career_goal']}")

    print()


# ===========================
# Main Menu
# ===========================

while True:

    print("=" * 40)
    print("        CareerPilot")
    print(" Student Profile Module")
    print("=" * 40)

    print("1. Create Student Profile")
    print("2. View Student Profiles")
    print("3. Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":

        create_profile()

    elif choice == "2":

        view_profiles()

    elif choice == "3":

        print("\nThank you for using CareerPilot.")
        break

    else:

        print("\nInvalid Choice! Please try again.\n")
def update_profile():
    """
    Update an existing student profile.
    """

    print("\n===== Update Student Profile =====")

    if len(students) == 0:
        print("No student profiles found.\n")
        return

    roll_no = input("Enter Roll Number to Update: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:

            print("\nStudent Found!")
            print("Press Enter to keep the current value.\n")

            name = input(f"Name ({student['name']}): ").strip()
            branch = input(f"Branch ({student['branch']}): ").strip()
            year = input(f"Year ({student['year']}): ").strip()
            career_goal = input(f"Career Goal ({student['career_goal']}): ").strip()

            if name:
                student["name"] = name
            if branch:
                student["branch"] = branch
            if year:
                student["year"] = year
            if career_goal:
                student["career_goal"] = career_goal

            print("\n✅ Student Profile Updated Successfully!\n")
            return

    print("\nStudent with this Roll Number not found!\n")

update_profile()
def delete_profile():
    """
    Delete an existing student profile.
    """

    print("\n===== Delete Student Profile =====")

    if len(students) == 0:
        print("No student profiles found.\n")
        return

    roll_no = input("Enter Roll Number to Delete: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("\n✅ Student Profile Deleted Successfully!\n")
            return

    print("\nStudent with this Roll Number not found!\n")
    delete_profile()