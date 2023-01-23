import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="jayzpkz",
    passwd="password",
    database="teskdatabase"
)

def department_summary(cursor, db):
    """
        List each department, even if it has no employees. Sort the
        results from high to low by number of employees, and then alphabetically by department if departments
        have the same number of employees. 
        
        :param cursor: cursor object connected to the database
        :param db: database object
        :return: rows data from the table after executing the query, otherwise None
    """
  
    try:
        # Select department name and number of employees working in the specified department (by id)
        # Join between Department and Employee tables while taking all the rows from the left table (Department) and only the matched rows from the right table (Employee)
        # Group by the department ID
        # Group by descending number of employees if equal, group by alphabetic order of department name
        query = """
            SELECT Department.NAME AS 'DEPT_NAME', COUNT(Employee.ID) AS 'EMP_COUNT'
            FROM {0}.Department
            LEFT JOIN {0}.Employee
            ON Department.ID = Employee.DEPT_ID
            GROUP BY Department.ID
            ORDER BY COUNT(Employee.ID) DESC, Department.NAME
        """.format(db.database)
        
        cursor.execute(query)

        return cursor.fetchall()
    except mysql.connector.Error as e:
        print("Couldn not execute the query.", e)
        return None
