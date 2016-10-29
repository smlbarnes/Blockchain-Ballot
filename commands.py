# Import custom modules
import app
import crypto

# Define the possible commands
commandMappings = {
    'help': app.outputHelp,
    'quit': app.quit
}

# Take an input and run the appropriate command (if valid)
def run(input):

    # Check if the given command exists in the mapping
    if input in commandMappings:

        # Get the given commands corresponding function
        commandFunction = commandMappings[input]

        # Call the appropriate command function
        commandFunction()

    else:

        # Display an invalid command messages
        print 'Invalid command given, use "help" to see list of valid arguments.'
