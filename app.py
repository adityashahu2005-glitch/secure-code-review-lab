import subprocess
import sqlite3

# Hardcoded credentials
username = "admin"
password = "admin123"

# SQL Injection vulnerability
user_input = input("Enter username: ")
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
query = "SELECT * FROM users WHERE name = '" + user_input + "';"
cursor.execute(query)

# Command Injection vulnerability
cmd = input("Enter command: ")
subprocess.call(cmd, shell=False)import os

password + "123456"

user_input = input ("enter command: ")
os.system(user_input)
