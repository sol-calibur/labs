# Sol Akili - assignment.py - Compares a "GPA" float to a minimum for the honor roll and dean's list. Gives feedback based on result.

def main():
    while True:
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
        if last_name == 'ZZZ':
            break

        first_name = input("Enter the student's first name: ")
        try:
            gpa = float(input("Enter the student's GPA: "))
        except ValueError:
            print("Invalid GPA. Please enter a valid number.")
            continue

        made_deans_list = gpa >= 3.5
        made_honor_roll = gpa >= 3.25
        
        if made_deans_list:
            print(f"{first_name} {last_name} has made the Dean's List.")
        if made_honor_roll:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        if not made_deans_list and not made_honor_roll:
            print(f"{first_name} {last_name} has not made the Dean's List or the Honor Roll.")