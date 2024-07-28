# Author: Hikmet Tenis
# Date: 07/28/2024
# Description: A pirate showed up in your room suddenly

# Ask pirate the password
# Print output using the input
# If it enters "Arrr!", print "Go Away, pirate"
# Otherwise print "Greetings, hater of pirates!"

# Prompt the user for a password input
greeting = input("Hello, possible pirate! What's the password? ")

# Check if the input is "Arrr!"
if greeting in ["Arrr!"]:
    # If the input matches "Arrr!", print this message
    print("Go away, pirate.")
else:
    # If the input does not match "Arrr!", print this message
    print("Greetings, hater of pirates!")

