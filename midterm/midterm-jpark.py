#!/usr/bin/env python3r
import sys
# Print out your first and last name to the screen in this format:
#print(“Name :<your first name> <your last name>”)

# In your script, initialize a dictionary named password_database that contains the following key:value pairs:
# Username:dnedry
# Password:please

# Initialize a dictionary named command_database that contains the following key:value pairs:
# reboot	: OK. I will reboot all park systems.
# shutdown	: OK. I will shut down all park systems.
# done		: I hate all this hacker stuff.

# Initialize two objects named white_rabbit_object and counter
# white_rabbit_object = 0
# Note: This is used to break out of the while loop
# counter = 0
# Note: This is used to count the number of failed authentication attempts

# Create a While Loop
# The primary goal of the while loop is to authenticate the user. You will use IF statements inside the while loop to make decisions about the
# authentication process. The while loop should use the counter object to determine how many authentication failures have occurred.
# When three authentication failures have occurred the script should print a unique message. The while loop should use the white_rabbit_object to
# identify a successful login.

# Start your while loop using a logical operator to evaluate the current values of white_rabbit_object and counter.
# Is white_rabbit_object equal to 0
# Is the value of counter less than 3

# Create two variables using input from the user
# input_user = 
# input_password =

# Use an IF statement to compare the user input against the values stored in the password_database dictionary
# If both the username and password are correct
# Set white_rabbit_object to 1
# Print “Hi, Dennis. You’re still the best hacker in Jurassic Park.”
# Ask the user to enter a command
# As part of this statement, print the keys in command_database to show the three available commands
# Evaluate the command provided by the user
# If the command is reboot print the associated value from command_database
# If the command is shutdown print the associated value from command_databasey

# If the command is done print the associated value from command_database
# For any other command, print “The Lysine Contingency has been put into effect.”
# Otherwise, If either the username or password are incorrect
# Increment counter by 1
# If the counter is equal to 3 print “You didn’t say the magic word” 25 times. Note: Each printed string should be on a new line. 
# Otherwise, print a formatted string that also shows the value of counter
# “You didn’t say the magic word.{counter}"

usuarios = dict()

password_database  = dict()
password_database["Username"] = "dnedry"
password_database["Password"] = "please"

command_database = dict()
command_database["reboot"] = "OK, I will reboot all park systems"
command_database["shutdown"] = "OK, I will shut down all park systems"
command_database["done"] = "I hate all this hacker stuff"

usuarios["dnedry"] = password_database

print("Name: <Marco> <Soberanes>")
counter = 0
usuario = password_database.get("Username")
contrasen = password_database.get("Password")
white_rabbit_object = 0
while True:
    if white_rabbit_object == 1:
         break
    if counter < 3:
        if white_rabbit_object == 0:
            input_user = input("Username: ")
            input_password = input("Password: ")
            if (usuario == input_user) \
                and (contrasen == input_password):    
                white_rabbit_object =1                       
                print("Hi Dennis, you are still the best Hacker in Jurassic Park!")
                input_command = input(f"Please enter a command [{command_database.keys()}] : " )
                if  input_command == "reboot":
                    print(command_database.get("reboot"))
                    break                    
                if  input_command == "shutdown":
                    print(command_database.get("shutdown"))
                    break                     
                if  input_command == "done":
                    print(command_database.get("done"))
                    break
                else:
                    print("The Lysine Contingency has been put into effect.!")
                    break
            else:
                counter = counter +1
    else:
       if counter == 3:
            print("You didn't say the magic word.\n" * 25)
            break
    if counter == 2:
        if white_rabbit_object != 1:
            print(f"You didn't say the magic word. {counter}")    
    if counter == 1:
        if white_rabbit_object != 1:
            print(f"You didn't say the magic word. {counter}") 
