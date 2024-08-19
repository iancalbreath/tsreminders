# Ian Calbreath
# Creating the .batch file that sends the reminder message + the cmd string + printing

# NEED TO ADD FREQUENCY SETTINGS (EVERY 15 MINUTES, ETC.)

import os
import re
import subprocess
from datetime import datetime
current_date = datetime.now().strftime("%Y-%m-%d.%H%M%S")

def get_user_input():
    # Prompt for username
    username = input("What is the username of the user that should be reminded? ")
    
    # Prompt for reminder message
    reminder_message = input("What is your reminder message? ")
    
    return username, reminder_message

def create_reminder_file(username, reminder_message):
    # Create a formatted message
    text_to_write = f'msg {username} "{reminder_message}"'
    
    # Create a file and write the message
    filename = f"{username}_reminder_{current_date}.bat"  # Creating a file name based on the username
    with open(filename, "w") as file:
        file.write(text_to_write)

    print(f"Reminder file '{filename}' created successfully.")

def get_reminder_schedule(username):
    # Prompt for reminder frequency
    reminder_frequency = input("How often do you want to be reminded? Options: daily, weekly, monthly. ").strip().lower()
    
    start_time_24hr = None  # Initialize variable
    if reminder_frequency == "daily":
        while True:
            # Prompt for start time and validate format
            start_time = input("When should the reminders start? (e.g., 08:00 AM) ").strip()
            try:
                # Convert to 24-hour format
                start_time_24hr = convert_to_24hr_format(start_time)
                break  # Exit loop if the format is correct
            except ValueError as e:
                print(e)  # Print the error message
                print("Please enter the time in the correct format (e.g., 08:00 AM).")
        
        # Create and print the schtasks command
        print("Here is the command line:  \n")
        command_line_d = f'schtasks /create /tn "{username}Reminder{current_date}" /tr "{username}_reminder_{current_date}.bat" /sc daily /st {start_time_24hr} \n'
        print(command_line_d)
        
        print_cmd = input("Do you want to print the command line to a file? (y/n)  \n").strip().lower()
        if print_cmd == "y":
            # Create a file and print the command line inside
            filename = f"PrintReminderD_{username}_{current_date}.txt"  # Creating a file name based on the username
            with open(filename, "w") as file:
                file.write(command_line_d)
                print(f'{filename} successfully printed. \n')
    
    elif reminder_frequency == "weekly":
        while True:
            # Get days of week from user
            day_of_week = input("What day(s) of the week should it run? ex. (MON,TUE,WED) ").strip()
            # Prompt for start time and validate format
            start_time = input("When should the reminders start? (e.g., 08:00 AM) ").strip()
            try:
                # Convert to 24-hour format
                start_time_24hr = convert_to_24hr_format(start_time)
                break  # Exit loop if the format is correct
            except ValueError as e:
                print(e)  # Print the error message
                print("Please enter the time in the correct format (e.g., 08:00 AM).")
        
        # Create and print the schtasks command
        print("Here is the command line:  \n")
        command_line_w = f'schtasks /create /tn "{username}Reminder{current_date}" /tr "{username}_reminder_{current_date}.bat" /sc weekly /d {day_of_week} /st {start_time_24hr} \n'
        print(command_line_w)
        
        print_cmd = input("Do you want to print the command line to a file? (y/n)  \n").strip().lower()
        if print_cmd == "y":
            # Create a file and print the command line inside
            filename = f"PrintReminderW_{username}_{current_date}.txt"  # Creating a file name based on the username
            with open(filename, "w") as file:
                file.write(command_line_w)
                print(f'{filename} successfully printed. \n')
    
    else:
        print("Invalid selection.")
    
    # Prompt for executing command line now
    register_task = input("Do you want me to register this task with Task Scheduler now? (y/n) ").strip().lower()
    if register_task == "y":
        # Execute the command
        if reminder_frequency == "daily":
            execute_command(command_line_d)
        elif reminder_frequency == "weekly":
            execute_command(command_line_w)

def execute_command(command_line):
    # Execute the command using subprocess
    try:
        result = subprocess.run(command_line, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Command executed successfully.")
        print("Output:", result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        print("An error occurred while executing the command.")
        print("Error:", e.stderr)




def convert_to_24hr_format(time_str):
    # Regular expression to match time format
    match = re.match(r"(\d{1,2}):(\d{2})\s*(AM|PM)", time_str, re.IGNORECASE)
    
    if match:
        hour, minute, period = match.groups()
        hour = int(hour)
        if period.upper() == "PM" and hour != 12:
            hour += 12
        elif period.upper() == "AM" and hour == 12:
            hour = 0
        return f"{hour:02}:{minute}"
    else:
        raise ValueError("Invalid time format. Please use HH:MM AM/PM.")

    
def main():
    # Get user inputs for username and reminder message
    username, reminder_message = get_user_input()
    
    # Create the reminder file with the provided information
    create_reminder_file(username, reminder_message)
    
    # Get the reminder frequency and start time
    get_reminder_schedule(username)  # Call without unpacking

if __name__ == "__main__":
    main()

