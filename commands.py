# Import required modules
import os

# Import custom modules
import app
import input
import output
import file
import ballot
import keys
import crypto

# Create a new ballot
def initaliseBallot():

    # Get the name of the ballot
    title = raw_input("Title of the ballot: ")

    # Get the description of the ballot
    description = raw_input("Description for the ballot: ")

    # Get the ballot candidates
    candidatesString = raw_input("Please enter the candidates separated by commas (','): ")
    candidates = candidatesString.split(",")

    # Get the voter addresses
    votersString = raw_input("Please enter the voter addresses separated by commas (','): ")
    voters = candidatesString.split(",")

    # Get the ballot public key
    publicKey = raw_input("Enter the public key of the ballot: ")

    # Initalise a ballot with the given values
    ballot.initalise(title, description, candidates, voters, publicKey)

# Generate and save a new set of keys
def newKey():

    # Get the name for the key
    keyName = raw_input("Please enter a name for the key: ")

    # Generate a new key pair
    publicKey, privateKey = crypto.generateKeyPair()

    # Save the key
    keys.saveKey(keyName, publicKey, privateKey)

    # Return control to the app
    print 'Key "' + keyName + '" saved.'

# List all the keys in the console
def listKeys():
    output.allKeys()

# Import a key
def importKey():

    # Get the path for the key file
    filePath = raw_input("Please give the path to the key file: ")

    # Import the key file at the given path
    keys.importKey(filePath)

    # Return control to the program
    print 'Key at "' + filePath + '" saved.'

# Export a key
def exportKey():

    # Show the saved keys and get the users selection
    keyToExport = input.getKeySelection()

    # Check if a key was selected
    if keyToExport == False:

        # Invalid index or name given
        print 'Key not found.'

    else:

        # Initalise the include private key flag
        includePrivateKey = False

        # Check if there is a private key
        if keyToExport.privateKey:

            # Check if the user wants to include the private key
            includePrivateKeyInput = raw_input("Do you want to include the private key? (y/n): ")

            # Set the flag according to the users response
            if includePrivateKeyInput == 'y':
                includePrivateKey = True
            else:
                includePrivateKey = False

        # Export the private key
        keys.export(keyToExport, includePrivateKey)

        # Return control to the program
        print 'Key "' + keyToExport.name + '" exported to: ' + os.getcwd() + '/' + keyToExport.name + ' Export.csv'

# Delete a key
def deleteKey():

    # Show the saved keys and get the users selection
    keyToDelete = input.getKeySelection()

    # Check if a key was selected
    if keyToDelete == False:

        # Invalid index or name given
        print 'Key not found.'

    else:

        # Delete the key
        keys.delete(keyToDelete)

        # Return control to the program
        print 'Key ' + keyToDelete.name + ' deleted.'

# Define the possible commands
commandMappings = {
    'init-ballot': initaliseBallot,
    'new-key': newKey,
    'list-keys': listKeys,
    'import-key': importKey,
    'export-key': exportKey,
    'delete-key': deleteKey,
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
