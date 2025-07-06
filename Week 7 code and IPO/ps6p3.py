def compute_trip_statistic(miles, gallons):
    if gallons > 0:
        mpg = miles / gallons
    else:
        mpg = 0.0
    cost = gallons * 3.00
    return mpg, cost

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
    total_miles = 0.0
    total_cost = 0.0
    trip_count = 0

    choice = get_yes_no("Please enter trip data? (yes/no): ")
    while choice == 'yes':
        dest = input("Enter destination city: ").strip()
        miles = get_valid_float("Enter miles travelled: ")
        gallons = get_valid_float("Enter gallons used: ")

        mpg, cost = compute_trip_statistic(miles, gallons)
        # Print the destination city, miles, MPG, gas cost
        print("Destination City:", dest)
        print("Miles:", miles)
        print("MPG:", mpg)
        print("Gas cost:", cost)

        trip_count += 1
        total_miles += miles
        total_cost += cost

        choice = get_yes_no("Continue? (yes/no): ")

    # Print out the number of entries, total miles travelled, and total gas cost
    print("\nNumber of entries:", trip_count)
    print("Total miles travelled:", total_miles)
    print("Total gas cost:", total_cost)

# The code to start the program
main()