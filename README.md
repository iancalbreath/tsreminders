# TSreminders
A user-friendly Python prompt to create reminders using Task Scheduler.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Usage](#usage)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)

## Project Overview
**Objective:**  
TSreminders is a Python-based tool that prompts users for input (username, reminder message, and reminder frequency) and converts this information into a Batch or Powershell command string. This command can be used to create a Task Scheduler task that sends custom reminders to users on a local Windows machine.  Optionally, the tool will implement the string for the user.

## Features
User Input Prompts: Asks for the username, reminder message, and reminder frequency.  
Command Generation: Converts input into a Batch or Powershell string.  
Task Scheduler Integration: Option to automatically create a scheduled task.  
Error Handling: Ensures that inputs are validated and handled gracefully.

## Usage
Run the program:
```bash
python tsreminders.py
```
  
Follow the prompts:  

Enter the username of the user to be reminded.  
Enter the reminder message.  
Specify the reminder frequency (e.g., daily, weekly).  
View or execute the generated command string:  

Option 1: Copy and paste the command string into your Batch or Powershell script.  
Option 2: Allow the program to automatically set up the task in Windows Task Scheduler.

### Overview
TSreminders is designed with simplicity and ease of use in mind. It follows a linear workflow:

User Input: Collects required information from the user.  
Validation: Ensures that all inputs are correct and formatted properly.  
Command Generation: Converts the validated input into a Task Scheduler-compatible command string.  
Execution (Optional): Provides the user with the command string or sets up the task automatically.

## Contribution Guidelines
We welcome contributions from the community! To contribute:

Fork the repository.
Create a new branch:
```bash
git checkout -b feature-name
```
Make your changes and commit them:
```bash
git commit -m "Description of changes"
```
Push to the branch:
```bash
git push origin feature-name
```
Create a pull request explaining your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
