# Blockchain Ballot
# Handcrafted by Samuel Barnes
print ''
print 'Blockchain Ballot | Version 0.1'
print ''

# TODO Check dependancies

 # Import required modules
import sys

# Import custom modules
import crypto

# Define the functions for the commands
# Function to print information and user help
def help():

    # Print information
    print 'A voting system built to run on the Ethereum network with Python used for local execution. Implements a paillier cryptosystem with the use of homomorphic addition to calculate the results without divulging individual voter decision.'
    print ''

    # Print the possible commands
    print 'Possible commands:'
    print 'help - Outputs this information.'

# Get arguments
arguments = sys.argv

# Get the first argument (if given)
if 1 < len(arguments):
    commandArgument = arguments[1]
else:
    # Set the default command
    commandArgument = 'help'

# Define the possible commands
commandMappings = {
    'help': help
}

# Check if the given command exists in the mapping
if commandArgument in commandMappings:

    # Get the given commands corresponding function
    commandFunction = commandMappings[commandArgument]

    # Call the appropriate command function
    commandFunction()

else:

    # Display an invalid command messages
    print 'Invalid command given, use "help" to see list of valid arguments.'

# Pad the output (for OCD reasons)
print ''
