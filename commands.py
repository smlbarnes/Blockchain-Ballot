# Import required modules
import os

# Import custom modules
import app
import input
import output
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
    voters = votersString.split(",")

    # Get the ballot public key
    print 'Select the key you want to use for the ballot.'
    key = input.getKeySelection()

    # Get the Ethereum account to use
    print 'Select the account you want to use for the ballot.'
    account = input.getAccountSelection()

    # Initalise a ballot with the given values
    ballot.initalise(account, title, description, candidates, voters, key)

# List the ballots in the console
def listBallots():
    output.allBallots()

# Get more information about a ballot
def ballotInfo():

    # Get the ballot
    print 'Select the ballot you wish to see more information about.'
    ballot = input.getBallotSelection()

    # Display the ballot information
    output.ballotInfo(ballot)

# Cast a vote
def castVote():

    # Get the ballot
    print 'Select the ballot you want to vote in.'
    selectedBallot = input.getBallotSelection()

    # Get the Ethereum account to use
    print 'Select the account you want to use to vote.'
    account = input.getAccountSelection()

    # Display the ballot information
    output.ballotInfo(selectedBallot, False, False)

    # Get the candidate to vote for
    print 'Select the candidate you wish to vote for.'
    candidate = input.getCandidateSelection(selectedBallot)

    # Build the vote to send
    vote = ballot.buildVote(selectedBallot, candidate)

    # Execute the vote
    ballot.executeVote(selectedBallot, account, vote)

# Import a ballot
def importBallot():

    # Get the path for the ballot file
    filePath = raw_input("Please give the path to the ballot file: ")

    # Import the ballot file at the given path
    ballot.importBallot(filePath)

    # Return control to the program
    print 'Ballot at "' + filePath + '" saved.'

# Export a ballot
def exportBallot():

    # Get the ballot
    print 'Select the ballot you wish to export.'
    ballotToExport = input.getBallotSelection()

    # Check if a ballot was selected
    if ballotToExport == False:

        # Invalid index or name given
        print 'Ballot not found.'

    else:

        # Export the ballot
        ballot.export(ballotToExport)

        # Return control to the program
        print 'Ballot "' + ballotToExport.title + '" exported to: ' + os.getcwd() + '/' + ballotToExport.title + ' Export.csv'

# Tally the votes of a ballot
def tallyResults():

    # Get the ballot
    ballotToTally = input.getBallotSelection()

    # Show the saved keys and get the users selection
    print 'Select the key used for the ballot. You need the private key to view the result.'
    key = input.getKeySelection()

    # Check that the user has the private key
    if (key.privateKey == False):

        # Alert the user they do not possess the private key
        print 'Private key not found for the selected key.'

    else:

        # Get the votes
        votes = ballot.getVotes(ballotToTally)

        # Calculate the result using the key
        results = crypto.addVotes(votes, key.publicKey)

        print 'Results: '
        for index in xrange(len(results)):
            print 'Candidate ' + str(index+1) + ': ' + str(crypto.decrypt(key.privateKey, results[index]))

# Delete a ballot
def deleteBallot():

    # Show the saved ballots and get the users selection
    ballotToDelete = input.getBallotSelection()

    # Check if a balloy was selected
    if ballotToDelete == False:

        # Invalid index or name given
        print 'Ballot not found.'

    else:

        # Delete the ballot
        ballot.delete(ballotToDelete)

        # Return control to the program
        print 'Ballot "' + ballotToDelete.title + '" deleted.'

# List the accounts in the console
def listAccounts():
    output.allAccounts()

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

# Test a key is working correctly
def testKey():

    # Show the saved keys and get the users selection
    keyToTest = input.getKeySelection()

    # Check if a key was selected
    if keyToTest == False:

        # Invalid index or name given
        print 'Key not found.'

    else:

        # Check the key can be tested (has private key)
        if keyToTest.privateKey:

            # Test the key can encrypt and decrypt an integer
            if keys.testEncryption(keyToTest):
                print 'Encryption test passed.'
            else:
                print 'Encryption test failed.'

            # Test the key can perform a homomorphic addition
            if keys.testHomomorphism(keyToTest):
                print 'Homomorphism test passed.'
            else:
                print 'Homomorphism test failed.'

            # Return control to the program
            print 'Test of key "' + keyToTest.name + '" complete.'

        else:

            # Inform the user the user there is not private key
            print 'Key cannot be tested as there is no private key.'

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
        print 'Key "' + keyToDelete.name + '" deleted.'

# Define the possible commands
commandMappings = {
    'init-ballot': initaliseBallot,
    'list-ballots': listBallots,
    'ballot-info': ballotInfo,
    'cast-vote': castVote,
    'import-ballot': importBallot,
    'export-ballot': exportBallot,
    'tally-results': tallyResults,
    'delete-ballot': deleteBallot,
    'list-accounts': listAccounts,
    'new-key': newKey,
    'list-keys': listKeys,
    'import-key': importKey,
    'export-key': exportKey,
    'test-key': testKey,
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
        print 'Invalid command given, use "help" to see list of valid commands.'
