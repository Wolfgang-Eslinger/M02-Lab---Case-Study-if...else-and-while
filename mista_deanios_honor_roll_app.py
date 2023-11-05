# Wolfgang Eslinger
# mista_deanios_honor_roll_app.py
# This app will take student names and GPAs and tests if the student qualifies for the Dean's List or the Honor Roll.

def process_students():
    """
    Process student records for Dean's List and Honor Roll qualification.
    The app stops processing when the last name 'ZZZ' is entered.
    """
    while True:
        # Ask for the student's last name
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ").strip()
        
        # Check if we should quit the process
        if last_name.upper() == 'ZZZ':
            break
        
        # Ask for the student's first name
        first_name = input("Enter the student's first name: ").strip()
        
        # Ask for the student's GPA as a float
        try:
            gpa = float(input("Enter the student's GPA: ").strip())
        except ValueError:
            print("Invalid GPA entered. Please enter a numeric value.")
            continue

        # Test for Dean's List qualification
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        # Test for Honor Roll qualification
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")

process_students()