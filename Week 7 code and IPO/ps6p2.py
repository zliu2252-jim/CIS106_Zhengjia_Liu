def compute_batting_average(hits, at_bats):
    if at_bats <= 0:
        return 0.0
    return hits / at_bats

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ('yes', 'no'):
            return choice
        print("Please enter 'yes' or 'no'.")

def main():
    player_count = 0
    choice = get_yes_no("Please enter player data? (yes/no): ")

    while choice == 'yes':
        last_name = input("Enter player's last name: ").strip()
        hits = get_valid_int("Enter number of hits: ")
        at_bats = get_valid_int("Enter number of at bats: ")

        average = compute_batting_average(hits, at_bats)
        # Print the last name nad batting average
        print("Last name:", last_name)
        print("Batting average:", average)

        player_count += 1
        choice = get_yes_no("Continue? (yes/no): ")

    print("Number of players entered:", player_count)

# The code to start the program
main()