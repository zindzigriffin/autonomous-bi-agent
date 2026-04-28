import sqlite3
import pandas as pd

def initialize_database():
    # Connect to SQLite database
    conn = sqlite3.connect("enterprise.db")
    cursor = conn.cursor()

    # Create a table for Regional Performance
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS performance (
            region TEXT,
            q3_revenue INTEGER,
            q4_revenue INTEGER,
            churn_rate REAL,
            customer_satisfaction REAL
        )
    ''')

    # Insert mock data
    mock_data = [
        ("North America", 500000, 450000, 0.08, 4.2),
        ("EMEA", 300000, 310000, 0.03, 4.8),
        ("APAC", 250000, 280000, 0.04, 4.5),
        ("LATAM", 150000, 120000, 0.12, 3.8)
    ]
    
    cursor.executemany("INSERT INTO performance VALUES (?, ?, ?, ?, ?)", mock_data)
    conn.commit()
    conn.close()
    print("Database initialized: enterprise.db created.")

if __name__ == "__main__":
    initialize_database()