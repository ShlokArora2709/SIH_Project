import mysql.connector
import pandas as pd

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",  # Replace with your MySQL host
    user="root",       # Replace with your MySQL username
    password="12345",  # Replace with your MySQL password
    database="cases"   # Replace with your database name
)

def main():
    # Get the Case ID from the user
    CaseID = input("Enter the Case ID: ")

    try:
        cursor = conn.cursor()

        # Query the database to retrieve case information
        cursor.execute("SELECT * FROM case_info WHERE case_id = %s", (CaseID,))
        result = cursor.fetchone()
        if result:
            print(result)
        else:
            print(f"Case {CaseID} not found.")

    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
