# Department Summary

Given 2 tables in a database (MySQL / PostgreSQL), Employee and Department, generate a summary <br>
of the # of employees in each department. List each department, even if it has no employees. Sort the <br>
results from high to low by number of employees, and then alphabetically by department if departments <br>
have the same number of employees. The results should list 1: department name and 2: employee count <br>
in appropriate column names.

#### Notes:

● Use the below schemas to create the required tables <br>
● Use an SQL query that renders the desired result

### Schema

#### EMPLOYEE:

    ID (Integer) - Employee ID number. This is a primary key.
    NAME (String) - Employee name
    SALARY (Integer) - Employee salary
    DEPT_ID (Integer) - ID of the employee's department, a foreign key to DEPARTMENT.ID.

#### DEPARTMENT:

    ID (Integer) - Department ID. This is a primary key.
    NAME (String) - Department name.
    LOCATION (String) - Department location.

### Sample Data Tables

![image](https://user-images.githubusercontent.com/57365299/214417975-396bdc99-4f7c-4702-b027-54064fc1689a.png)

### Sample Output

![image](https://user-images.githubusercontent.com/57365299/214418113-2b38df6d-b847-4fde-942a-de3e8597099c.png)

<br>
