import mysql.connector

def delete_tables(cursor, db):
    """
        This method delete "Department" and "Employee" tables
        :param cursor: cursor object connected to the database
        :param db: database object
        :return: True if data was deleted successfully, False otherwise
    """
    
    try:
        # Check if Employee table already exists
        cursor.execute("SHOW TABLES LIKE {0}.Employee".format(db.database))
        if cursor.fetchone():
            # Delete Employee table
            cursor.execute("DROP TABLE {0}.Employee".format(db.database))
        else:
            print("Employee table does not exist")
            
        # Check if Department table already exists
        cursor.execute("SHOW TABLES LIKE {0}.Department".format(db.database))
        if cursor.fetchone():
            # Delete Department table
            cursor.execute("DROP TABLE {0}.Department".format(db.database))
        else:
            print("Department table does not exist")
            
        # Commit the transaction
        db.commit()
    except mysql.connector.Error as e:
        print("Failed to delete tables.", e)

def delete_test_data(cursor, db):
    """
        This method delete test data from "Department" and "Employee" tables
        :param cursor: cursor object connected to the database
        :param db: database object
        :return: True if data was deleted successfully, False otherwise
    """
    
    try:
        # Delete all data from the Employee table
        cursor.execute("DELETE FROM {0}.Employee".format(db.database))
        
        # Delete all data from the Department table
        cursor.execute("DELETE FROM {0}.Department".format(db.database))
        
        # Commit the transaction
        db.commit()
        
        return True
    except mysql.connector.Error as e:
        print("Failed to delete test data.", e)
        return False
        

def insert_test_data(cursor, db):
    """
        This method inserts test data into "Department" and "Employee" tables
        :param cursor: cursor object connected to the database
        :param db: database object
        :return: True if tables were created successfully, False otherwise
    """
    
    department_data = [
        (1, 'Executive', 'Sydney'),
        (2, 'Production', 'Sydney'),
        (3, 'Resources', 'Cape Town'),
        (4, 'Technical', 'Texas'),
        (5, 'Management', 'Paris')
    ]

    department_query = "INSERT INTO {0}.Department (ID, NAME, LOCATION) VALUES (%s, %s, %s)".format(db.database)
    
    employee_data = [
        (1, 'Candice', 4685, 1),
        (2, 'Julia', 2559, 2),
        (3, 'Bob', 4405, 4),
        (4, 'Scarlet', 2350, 1),
        (5, 'Ileana', 1151, 4)
    ]

    employee_query  = "INSERT INTO {0}.Employee (ID, NAME, SALARY, DEPT_ID) VALUES (%s, %s, %s, %s)".format(db.database)

    try:
        # Insert data into the Department table
        cursor.executemany(department_query, department_data)
        
        # Insert data into the Employee table
        cursor.executemany(employee_query, employee_data)
        
        # Commit the transaction
        db.commit() 
        
        return True
    except mysql.connector.Error as e:
        if e.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
            # Value already exists
            print("Value already exists!")
            return False
        else:
            # Other sql errors
            print("Failed to insert values:", e)
            db.rollback()
            return False
        
def create_tables(cursor, db):
    """
        This method creates the "Department" and "Employee" tables in the database
        :param cursor: cursor object connected to the database
        :param db: database object
        :return: True if tables were created successfully, False otherwise
    """

    department_table = """
    CREATE TABLE {0}.Department (
        ID INT PRIMARY KEY,
        NAME VARCHAR(255),
        LOCATION VARCHAR(255)
    )
    """.format(db.database)
    
    employee_table = """
    CREATE TABLE {0}.Employee (
        ID INT PRIMARY KEY,
        NAME VARCHAR(255),
        SALARY INT,
        DEPT_ID INT,
        FOREIGN KEY (DEPT_ID) REFERENCES {0}.Department(ID)
    )
    """.format(db.database)

    try:
        # Create the Department table
        cursor.execute(department_table)
        
        # Create the Employee table
        cursor.execute(employee_table)
        
        # Commit the transaction
        db.commit() 
        
        return True
    except mysql.connector.Error as e:
        if e.errno == mysql.connector.errorcode.ER_TABLE_EXISTS_ERROR:
            # Table is already exists
            print("Table is already exists!")
            return False
        else:
            # Other sql errors
            print("Table creation failed!", e)
            return False