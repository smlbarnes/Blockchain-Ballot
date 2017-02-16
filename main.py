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
import geth

# Check if a geth instance with rpc is running
if not geth.rpcRunning():

    # Show a warning
    print ''
    print 'WARNING! Geth instance either not running or doesn\'t have rpc enabled.'

# Main program loop
while True:

    # Show the console and take user input
    print ''
    input = raw_input("> ")
    print ''

    # Attempt to run the given command
    commands.run(input)
