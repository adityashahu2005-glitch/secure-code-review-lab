import subprocess

password = "Admin@123"

def run():
    user_input = input("Enter command: ")
    subprocess.call(user_input, shell=True)
