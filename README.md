# TSreminders
A user-friendly Python prompt to create reminders using Task Scheduler.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Design & Architecture](#design--architecture)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)

## Project Overview
**Objective:**  
The Reminder Program is a Python-based tool that prompts users for input (username, reminder message, and reminder frequency) and converts this information into a Batch or Powershell command string. This command can be used to create a Task Scheduler task that sends custom reminders to users on a local Windows machine.  Optionally, the tool will automatically implement the string.

## Features
- **User Input Prompts:** Asks for the username, reminder message, and reminder frequency.
- **Command Generation:** Converts input into a Batch or Powershell string that Task Scheduler recognizes.
- **Command Implementation:** Optionally pushes the string into Task Scheduler automatically.
- **Error Handling:** Ensures that inputs are validated and handled gracefully.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/reminder-program.git
