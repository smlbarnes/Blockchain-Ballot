# Blockchain Ballot
# Handcrafted by Samuel Barnes
print ''
print 'Blockchain Ballot | Version 0.1'

# TODO Check dependancies

 # Import required modules
import sys

# Import custom modules
import app
import crypto
import commands

# Main program loop
while True:

    # Show the console and take user input
    print ''
    input = raw_input("> ")

    # Attempt to run the given command
    commands.run(input)
