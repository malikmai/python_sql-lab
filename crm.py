import psycopg2
from psycopg2 import sql

# Database connection
conn = psycopg2.connect(
    dbname="company_db",
    user="jhnybkwd", 
    password="3xP3c+u$1428",
    host="localhost"
)
cursor = conn.cursor()

def create_company():
    name = input("Enter company name: ")
    address = input("Enter company address: ")
    city = input("Enter company city: ")
    state = input("Enter company state: ")
    country = input("Enter company country: ")
    phone = input("Enter company phone: ")
    website = input("Enter company website: ")

    cursor.execute(
        "INSERT INTO companies (name, address, city, state, country, phone, website) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (name, address, city, state, country, phone, website)
    )
    conn.commit()
    print("Company created successfully.")

def read_companies():
    cursor.execute("SELECT * FROM companies")
    companies = cursor.fetchall()
    for company in companies:
        print(company)

def update_company():
    company_id = input("Enter company ID to update: ")
    name = input("Enter new company name: ")
    address = input("Enter new company address: ")
    city = input("Enter new company city: ")
    state = input("Enter new company state: ")
    country = input("Enter new company country: ")
    phone = input("Enter new company phone: ")
    website = input("Enter new company website: ")

    cursor.execute(
        "UPDATE companies SET name=%s, address=%s, city=%s, state=%s, country=%s, phone=%s, website=%s WHERE company_id=%s",
        (name, address, city, state, country, phone, website, company_id)
    )
    conn.commit()
    print("Company updated successfully.")

def delete_company():
    company_id = input("Enter company ID to delete: ")
    cursor.execute("DELETE FROM companies WHERE company_id=%s", (company_id,))
    conn.commit()
    print("Company deleted successfully.")

def create_employee():
    first_name = input("Enter employee first name: ")
    last_name = input("Enter employee last name: ")
    email = input("Enter employee email: ")
    phone = input("Enter employee phone: ")
    hire_date = input("Enter hire date (YYYY-MM-DD): ")
    job_title = input("Enter job title: ")
    salary = input("Enter salary: ")
    company_id = input("Enter company ID: ")

    cursor.execute(
        "INSERT INTO employees (first_name, last_name, email, phone, hire_date, job_title, salary, company_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (first_name, last_name, email, phone, hire_date, job_title, salary, company_id)
    )
    conn.commit()
    print("Employee created successfully.")

def read_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    for employee in employees:
        print(employee)

def update_employee():
    employee_id = input("Enter employee ID to update: ")
    first_name = input("Enter new first name: ")
    last_name = input("Enter new last name: ")
    email = input("Enter new email: ")
    phone = input("Enter new phone: ")
    hire_date = input("Enter new hire date (YYYY-MM-DD): ")
    job_title = input("Enter new job title: ")
    salary = input("Enter new salary: ")
    company_id = input("Enter new company ID: ")

    cursor.execute(
        "UPDATE employees SET first_name=%s, last_name=%s, email=%s, phone=%s, hire_date=%s, job_title=%s, salary=%s, company_id=%s WHERE employee_id=%s",
        (first_name, last_name, email, phone, hire_date, job_title, salary, company_id, employee_id)
    )
    conn.commit()
    print("Employee updated successfully.")

def delete_employee():
    employee_id = input("Enter employee ID to delete: ")
    cursor.execute("DELETE FROM employees WHERE employee_id=%s", (employee_id,))
    conn.commit()
    print("Employee deleted successfully.")

def main():
    while True:
        print("\nCRM Tool")
        print("1. Create Company")
        print("2. Read Companies")
        print("3. Update Company")
        print("4. Delete Company")
        print("5. Create Employee")
        print("6. Read Employees")
        print("7. Update Employee")
        print("8. Delete Employee")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_company()
        elif choice == '2':
            read_companies()
        elif choice == '3':
            update_company()
        elif choice == '4':
            delete_company()
        elif choice == '5':
            create_employee()
        elif choice == '6':
            read_employees()
        elif choice == '7':
            update_employee()
        elif choice == '8':
            delete_employee()
        elif choice == '9':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

# Close the cursor and connection
cursor.close()
conn.close()