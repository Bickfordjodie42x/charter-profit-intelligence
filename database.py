
print("RUNNING FILE")
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


# ---------- RUN PROGRAM ----------

create_table()

# Test entry
save_trip(
    trip_price=900,
    fuel_cost=120,
    maintenance_cost=50,
    bait_cost=40,
    fixed_overhead=100
)
