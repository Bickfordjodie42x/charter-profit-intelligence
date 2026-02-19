
import sqlite3
from datetime import datetime


def create_connection():
    return sqlite3.connect("charter_data.db")


def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trips (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        trip_price REAL,
        fuel_cost REAL,
        maintenance_cost REAL,
        bait_cost REAL,
        fixed_overhead REAL,
        total_cost REAL,
        profit REAL,
        profit_margin REAL,
        trip_date TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_trip(trip_price, fuel_cost, maintenance_cost, bait_cost, fixed_overhead):
    total_cost = fuel_cost + maintenance_cost + bait_cost + fixed_overhead
    profit = trip_price - total_cost
    profit_margin = (profit / trip_price) * 100 if trip_price != 0 else 0
    trip_date = datetime.now().strftime("%Y-%m-%d")

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO trips 
    (trip_price, fuel_cost, maintenance_cost, bait_cost, fixed_overhead,
     total_cost, profit, profit_margin, trip_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        trip_price,
        fuel_cost,
        maintenance_cost,
        bait_cost,
        fixed_overhead,
        total_cost,
        profit,
        profit_margin,
        trip_date
    ))

    conn.commit()
    conn.close()

    print("Trip saved successfully.")
    print(f"Total Cost: ${total_cost}")
    print(f"Profit: ${profit}")
    print(f"Profit Margin: {profit_margin:.2f}%")




def show_summary():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*),
               SUM(trip_price),
               SUM(total_cost),
               SUM(profit),
               AVG(profit_margin)
        FROM trips
    """)
    result = cursor.fetchone()

    conn.close()

    if result[0] == 0:
        print("\nNo trips recorded yet.\n")
        return

    print("\n------ SUMMARY REPORT ------")
    print(f"Total Trips: {result[0]}")
    print(f"Total Revenue: ${result[1]:.2f}")
    print(f"Total Costs: ${result[2]:.2f}")
    print(f"Total Profit: ${result[3]:.2f}")
    print(f"Average Profit Margin: {result[4]:.2f}%")
    print("-----------------------------\n")


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


