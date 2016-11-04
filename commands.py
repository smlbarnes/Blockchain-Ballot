# Import custom modules
import app
import file
import ballot
import crypto

# Define the possible commands
commandMappings = {
    'init-ballot': ballot.initalise,
    'generate-key': crypto.generateNewKey,
    'list-keys': crypto.listKeys,
    'import-key': file.importKey,
    'export-key': file.exportKey,
    'delete-key': file.deleteKey,
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
