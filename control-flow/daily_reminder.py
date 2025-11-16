# daily_reminder.py
# Personal Daily Reminder

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        priority_text = "high priority task"
    case "medium":
        priority_text = "medium priority task"
    case "low":
        priority_text = "low priority task"
    case _:
        priority_text = "task with undefined priority"

if time_bound == "yes" and priority in ["high", "medium", "low"]:
    print(f"Reminder: '{task}' is a {priority_text} that requires immediate attention today!")
elif time_bound == "no" and priority in ["high", "medium", "low"]:
    print(f"Note: '{task}' is a {priority_text}. Consider completing it when you have free time.")
else:
    print(f"'{task}' has an undefined priority or time-bound status.")
