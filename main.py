from database import create_table, save_trip
from reports import show_summary


def main():
    while True:
        print("\nCharter Profit System")
        print("----------------------")
        print("1. Enter New Trip")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            try:
                trip_price = float(input("Trip Price: "))
                fuel_cost = float(input("Fuel Cost: "))
                maintenance_cost = float(input("Maintenance Cost: "))
                bait_cost = float(input("Bait Cost: "))
                fixed_overhead = float(input("Fixed Overhead: "))

                save_trip(
                    trip_price,
                    fuel_cost,
                    maintenance_cost,
                    bait_cost,
                    fixed_overhead
                )

                print("Trip saved successfully.")

            except ValueError:
                print("Invalid number entered. Try again.")

        elif choice == "2":
            show_summary()

        elif choice == "3":
            print("Exiting system.")
            break

        else:
            print("Invalid selection.")


if __name__ == "__main__":
    create_table()
    main()
