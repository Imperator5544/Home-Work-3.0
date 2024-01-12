"""
Користувач вводить із клавіатури номер дня тижня (1-7).
Необхідно вивести на екран назви дня тижня.
Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.
"""

try:
    day_number = int(input("Enter the day of the week number (1-7): "))
except ValueError:
    print("Please enter a valid number.")


match day_number:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("An incorrect day of the week number was entered. Please enter a number from 1 to 7.")
