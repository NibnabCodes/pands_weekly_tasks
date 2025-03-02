# weekday.py
# This program outputs whether or not today is a weekday.
# Source Used: https://chatgpt.com/share/67c48614-133c-8011-97f4-d427a4568b8a
# author: Niamh Hogan

# Import the datetime module
import datetime

# Get the current date.
today = datetime.date.today()

# Check if today is a weekday (Mon = 0, Sun = 6)
if today.weekday() < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")