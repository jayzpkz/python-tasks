from department_summary import department_summary
from utils import delete_test_data
from utils import insert_test_data
from utils import delete_tables
from utils import create_tables
import mysql.connector

def test_department_summary():
    """
    This function tests the department_summary function by creating tables, inserting test data, calling department_summary function, 
    asserting that the output is correct, cleaning up the data and then cleaning up the tables.

    :return: None
    """
    
    # Connect to the database
    db = mysql.connector.connect(
    host="localhost",
    user="jayzpkz",
    passwd="password",
    database="teskdatabase"
    )

    # Create cursor
    mycursor = db.cursor()
    
    # Create tables
    create_tables(mycursor, db)

    # Insert test data into the Employee and Department tables
    insert_test_data(mycursor, db)

    result = department_summary(mycursor, db)

    # Assert that the result is the expected output
    expected_output = [
        ('Executive', 2), 
        ('Technical', 2),
        ('Production', 1), 
        ('Management', 0), 
        ('Resources', 0)
    ]

    assert result == expected_output
    
    # Delete all data from Employee and Department tables
    delete_test_data(mycursor, db)
    
    # Delete tables
    delete_tables(mycursor, db)

    # Close the cursor and connection
    mycursor.close()
    db.close()
    
    
#! Would be good to add tests for the utility functions
