import sqlite3


def create_connection():
    conn = sqlite3.connect("charter_data.db")
    return conn


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
        profit_margin REAL
    )
    """)

    conn.commit()
    conn.close()

def save_trip(trip_price, fuel_cost, maintenance_cost, bait_cost, fixed_overhead, total_cost, profit, profit_margin):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO trips 
    (trip_price, fuel_cost, maintenance_cost, bait_cost, fixed_overhead, total_cost, profit, profit_margin)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (trip_price, fuel_cost, maintenance_cost, bait_cost, fixed_overhead, total_cost, profit, profit_margin))

    conn.commit()
    conn.close()


def get_all_trips():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM trips")
    rows = cursor.fetchall()

    conn.close()
    return rows


def get_profit_summary():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(profit), AVG(profit_margin) FROM trips")
    summary = cursor.fetchone()

    conn.close()
    return summary
