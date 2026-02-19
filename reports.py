from database import create_connection


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
