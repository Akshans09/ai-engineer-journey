import sqlite3
import pandas as pd

# Setup — run this once to create database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create tables
cursor.executescript("""
    DROP TABLE IF EXISTS employees;
    DROP TABLE IF EXISTS projects;
    
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        experience REAL,
        salary REAL,
        rating REAL
    );
    
    CREATE TABLE projects (
        id INTEGER PRIMARY KEY,
        project_name TEXT,
        employee_id INTEGER,
        status TEXT
    );
    
    INSERT INTO employees VALUES
        (1, 'Alice', 'ML', 3, 70000, 4.5),
        (2, 'Bob', 'Data', 5, 80000, 3.8),
        (3, 'Charlie', 'ML', 8, 90000, 4.2),
        (4, 'David', 'Data', 2, 55000, 4.9),
        (5, 'Eva', 'ML', 6, 85000, 3.5),
        (6, 'Frank', 'Data', 1, 48000, 4.1);
    
    INSERT INTO projects VALUES
        (1, 'LLM Chatbot', 1, 'active'),
        (2, 'RAG System', 2, 'active'),
        (3, 'CV Model', 3, 'completed'),
        (4, 'Data Pipeline', 5, 'active'),
        (5, 'Fine-tuning', 1, 'completed');
""")
conn.commit()

# ---- TASK 1 ----
# Get all employees in the ML department
# Use pd.read_sql_query and print the result

df = pd.read_sql_query("SELECT * FROM employees WHERE department = 'ML'",conn)
print(df)

# ---- TASK 2 ----
# Get name and salary of employees earning more than 70000
# Order by salary descending

df1=pd.read_sql_query("SELECT name,salary FROM employees WHERE salary> 70000 ORDER BY salary DESC", conn)
print(df1)
# ---- TASK 3 ----
# Get average salary and count per department
# Column names: department, avg_salary, employee_count

df2=pd.read_sql_query("SELECT department, AVG(salary) as avg_salary, COUNT(*) as employee_count FROM employees GROUP BY department",conn)
print(df2)

# ---- TASK 4 ----
# Get only departments where average salary > 70000
# Hint: HAVING clause

df3=pd.read_sql_query("SELECT department,AVG(salary) FROM employees GROUP BY department HAVING AVG(salary) > 70000",conn)
print(df3)

# ---- TASK 5 ----
# JOIN employees and projects
# Show employee name, their project name, and project status
# Only show active projects

df4=pd.read_sql_query("SELECT name,project_name,status FROM employees e JOIN projects p ON e.id = p.employee_id WHERE status = 'active'", conn)
print(df4)

# ---- TASK 6 ----
# Find employees who have NO projects assigned
# Hint: LEFT JOIN + WHERE project IS NULL

df5=pd.read_sql_query("SELECT name FROM employees e LEFT JOIN projects p ON e.id = p.employee_id WHERE p.employee_id IS NULL",conn)
print(df5)

conn.close()