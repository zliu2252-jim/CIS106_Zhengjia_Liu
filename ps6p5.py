def compute_tuition(credits, code):
    code = code.strip().upper()
    if code == 'I':
        rate = 250.0
    elif code == 'O':
        rate = 550.0
    else:
        rate = 0.0
    return credits * rate

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_valid_code(prompt):
    while True:
        code = input(prompt).strip().upper()
        if code in ('I', 'O'):
            return code
        print("Invalid code. Please enter 'I' or 'O'.")

def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ('yes', 'no'):
            return choice
        print("Please enter 'yes' or 'no'.")

def main():
    total_tuition = 0.0
    choice = get_yes_no("Please enter student data? (yes/no): ")

    while choice == 'yes':
        last_name = input("Enter student's last name: ").strip()
        credits = get_valid_int("Enter credit hours: ")
        district_code = get_valid_code("Enter district code (I/O): ")

        tuition = compute_tuition(credits, district_code)
        # Print last name and tuition owned
        print("Last name:", last_name)
        print("Tuition owed:", tuition)

        total_tuition += tuition
        choice = get_yes_no("Continue? (yes/no): ")

    print("\nTotal of all tuition owed:", total_tuition)

# The code to start the program
main()