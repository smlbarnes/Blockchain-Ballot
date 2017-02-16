# Print application information and user help
def outputHelp():

    # Print information
    print 'A voting system built to run on the Ethereum network with Python used for local execution. Implements a paillier cryptosystem with the use of homomorphic addition to calculate the results without divulging individual voter decision.'
    print ''

    # Print the possible commands
    print 'Commands:'
    print 'init-ballot - Create a new ballot.'
    print 'list-ballots - List the ballots on the system.'
    print 'ballot-info - Get the details of a ballot.'
    print 'cast-vote - Cast a vote within a ballot.'
    print 'import-ballot - Import a ballot from a file.'
    print 'export-ballot - Export a ballot to a file.'
    print 'tally-results - Get the results of a ballot.'
    print 'delete-ballot - Delete a saved ballot.'
    print 'list-accounts - List the local Ethereum accounts.'
    print 'new-key - Generate a new key pair.'
    print 'list-keys - List the keys on the system.'
    print 'import-key - Import a key from a file.'
    print 'export-key - Export a key to a file.'
    print 'test-key - Test a key is working correctly'
    print 'delete-key - Delete a saved key.'
    print 'help - Outputs this information.'
    print 'quit - Quits the program.'

# Quit the program
def quit():
    exit()
