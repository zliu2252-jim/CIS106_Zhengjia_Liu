def compute_extended_price(quantity, unit_price):
    extended_price = quantity * unit_price

    if extended_price > 100000.00:
        discount = extended_price * 0.10
    else:
        discount = 0.0
    return extended_price - discount

def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ('yes', 'no'):
            return choice
        print("Please enter 'yes' or 'no'.")

def main():
    total_extended_price = 0.0
    choice = get_yes_no("Do you want to compute extended price? (yes/no): ")

    while choice == 'yes':
        quantity = get_valid_float("Enter quantity: ")
        unit_price = get_valid_float("Enter unit price: ")

        extended_price = compute_extended_price(quantity, unit_price)
        # print the quantity, unit price, and the extended price
        print("Quantity:", quantity)
        print("Unit price:", unit_price)
        print("Extended Price:", extended_price)

        total_extended_price += extended_price
        choice = get_yes_no("Continue? (yes/no): ")

    # Make the total extended price displayed
    print("Total of all extended prices:", total_extended_price)

# The code to start the program
main()