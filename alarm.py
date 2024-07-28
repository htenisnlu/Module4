# Author: Hikmet Tenis
# Date: 07/28/2024
# Description: You need to get up early

# Ask the current hour and ask how long want to wait
# Calculate the wait time
# Print what time alarm is going to go off

# Prompt the user to enter the current time in hours (0-23)
str_time = input("What time is it now? ")

# Prompt the user to enter the number of hours to wait
str_wait_time = input("What is the number of hours to wait? ")

# Convert the current time from string to integer
time = int(str_time)

# Convert the wait time from string to integer
wait_time = int(str_wait_time)

# Calculate the time when the alarm will go off
time_when_alarm_go_off = (time + wait_time) % 24

# Convert the final time to hours and minutes (if applicable)
hours, minutes = divmod(time_when_alarm_go_off * 60, 60)

# Format the time as a string with leading zeros if necessary
formatted_time = f"{hours:02}:{minutes:02}"

# Print the time when the alarm will go off
print("The alarm will go off at:", formatted_time)

