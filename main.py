# Blockchain Ballot
# Handcrafted by Samuel Barnes
print ''
print 'Blockchain Ballot | Version 0.1'

# TODO Check dependancies

 # Import required modules
import sys

# Set system flags
sys.dont_write_bytecode = True

# Import custom modules
import app
import ballot
import crypto
import commands

# Main program loop
while True:

    # Show the console and take user input
    print ''
    input = raw_input("> ")
    print ''

    # Attempt to run the given command
    commands.run(input)
