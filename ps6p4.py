def compute_pay(job_code, hours):
    code = job_code.strip().upper()
    if code == 'L':
        rate = 25.0
    elif code == 'A':
        rate = 30.0
    elif code == 'J':
        rate = 50.0
    else:
        rate = 0.0

    if hours > 40:
        regular = 40 * rate
        overtime = (hours - 40) * rate * 1.5
        gross = regular + overtime
    else:
        gross = hours * rate

    return rate, gross

def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_valid_job_code(prompt):
    while True:
        code = input(prompt).strip().upper()
        if code in ('L', 'A', 'J'):
            return code
        print("Invalid job code. Enter L, A, or J.")

def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ('yes', 'no'):
            return choice
        print("Please enter 'yes' or 'no'.")

def main():
    total_gross = 0.0
    choice = get_yes_no("Do you want to compute pay? (yes/no): ")

    while choice == 'yes':
        last_name = input("Enter employee last name: ").strip()
        job_code = get_valid_job_code("Enter job code (L/A/J): ")
        hours = get_valid_float("Enter hours worked: ")

        rate, gross = compute_pay(job_code, hours)
        # Print last name, hours, pay rate, gross pay
        print("Last name:", last_name)
        print("Hours:", hours)
        print("Pay rate:", rate)
        print("Gross pay:", gross)

        total_gross += gross
        choice = get_yes_no("Continue? (yes/no): ")

    print("\nTotal of all gross pay:", total_gross)

# The code to start the program
main()