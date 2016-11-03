# Print application information and user help
def outputHelp():

    # Print information
    print 'A voting system built to run on the Ethereum network with Python used for local execution. Implements a paillier cryptosystem with the use of homomorphic addition to calculate the results without divulging individual voter decision.'
    print ''

    # Print the possible commands
    print 'Commands:'
    print 'init-ballot - Initalise a new ballot.'
    print 'list-keys - List the keys on the system.'
    print 'import-key - Import a key from a file.'
    print 'export-key - Export a key to a file.'
    print 'generate-key - Generate a new key pair.'
    print 'help - Outputs this information.'
    print 'quit - Quits the program.'

# Quit the program
def quit():
    exit()
