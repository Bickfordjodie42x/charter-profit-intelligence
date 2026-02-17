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
