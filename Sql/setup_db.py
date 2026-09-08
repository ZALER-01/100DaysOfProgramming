import sqlite3

# 1. Connect to a database file (creates it if it doesn't exist)
connection = sqlite3.connect("practice.db")
cursor = connection.cursor()

# 2. Create the CITY table (similar to HackerRank/LeetCode schemas)
cursor.execute("""
CREATE TABLE IF NOT EXISTS CITY (
    ID INTEGER PRIMARY KEY,
    NAME TEXT,
    COUNTRYCODE TEXT,
    DISTRICT TEXT,
    POPULATION INTEGER
)
""")

# 3. Clear old data and insert fresh practice rows
cursor.execute("DELETE FROM CITY")
sample_data = [
    (6, 'Rotterdam', 'NLD', 'Zuid-Holland', 593321),
    (3878, 'Scottsdale', 'USA', 'Arizona', 202705),
    (3965, 'Corona', 'USA', 'California', 124966),
    (3973, 'Concord', 'USA', 'California', 121780),
    (4054, 'Fairfield', 'USA', 'California', 92256)
]
cursor.executemany("INSERT INTO CITY VALUES (?, ?, ?, ?, ?)", sample_data)
connection.commit()

# 4. === WRITE AND RUN YOUR SQL QUERY HERE ===
query = """
SELECT SUM(POPULATION) FROM CITY 
WHERE DISTRICT LIKE '%Cali%';
"""

cursor.execute(query)
result = cursor.fetchall()

# 5. Print out the results
print("--- SQL Query Result ---")
for row in result:
    print(row)

# Close the database connection
connection.close()


