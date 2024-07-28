# Author: Hikmet Tenis
# Date: 07/28/2024
# Description: You are in DMV to renew your License but time is essense

# Ask the current hour and ask how long want to wait
# Calculate the wait time
# Print what time its going to be after waiting

# Prompt the user to enter the current time in hours (0-23)
current_time_str = input("What is the current time (in hours 0-23)? ")

# Prompt the user to enter the number of hours they want to wait
wait_time_str = input("How many hours do you want to wait? ")

# Convert the current time from string to integer
current_time_int = int(current_time_str)

# Convert the wait time from string to integer
wait_time_int = int(wait_time_str)

# Calculate the final time by adding the current time and wait time
final_time_int = (current_time_int + wait_time_int) % 24 

# Convert the final time to hours and minutes (if applicable)
hours, minutes = divmod(final_time_int * 60, 60)

# Format the time as a string with leading zeros if necessary
formatted_time = f"{hours:02}:{minutes:02}"

# Print the final time
print("The time after waiting will be:", formatted_time)
