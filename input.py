# Import custom modules
import output
import ballot
import keys
import geth

# Get a saved ballot of the user's choice
def getBallotSelection():

    # Show a list of all the ballots with indexes
    output.allBallots(True)

    # Ask the user which ballot they want to select
    print ''
    ballotId = raw_input("Please enter the name or number of the ballot you want to select: ")

    # Get the data type of the input
    inputType = checkInputType(ballotId)

    # Retrive the saved ballot by index
    if inputType == 'integer':
        return ballot.getBallotByIndex(int(ballotId) - 1)

    # Retrive the ballot key by name
    if inputType == 'string':
        return ballot.getBallotByName(ballotId)

# Get a saved key of the user's choice
def getKeySelection():

    # Show a list of all keys with indexes
    output.allKeys(True)

    # Ask the user which key they want to select
    print ''
    keyId = raw_input("Please enter the name or number of the key you want to select: ")

    # Get the data type of the input
    inputType = checkInputType(keyId)

    # Retrive the saved key by index
    if inputType == 'integer':
        return keys.getKeyByIndex(int(keyId) - 1)

    # Retrive the saved key by name
    if inputType == 'string':
        return keys.getKeyByName(keyId)

# Get an Ethereum account of the users choice
def getAccountSelection():

    # Show all the local Ethereum accounts with index
    output.allAccounts(True)

    # Ask the user which account they want to select
    print ''
    accountId = raw_input("Please enter the address or number of the account you want to select: ")

    # Get the data type of the input
    inputType = checkInputType(accountId)

    # Retrive the account by index
    if inputType == 'integer':
        return geth.getAccountByIndex(int(accountId) - 1)

    # Retrive the account by address
    if inputType == 'string':
        return geth.getAccountByAddress(accountId)

# Get a ballot candidate of the users choice
def getCandidateSelection(selectedBallot):

    # Show all the candidates of the ballot
    output.candidates(selectedBallot)

    # Ask the user which candidates they want to select
    print ''
    candidateId = raw_input("Please enter the name or number of the candidate you want to select: ")

    # Get the data type of the input
    inputType = checkInputType(candidateId)

    # Return the candidates index
    if inputType == 'integer':
        return int(candidateId) - 1

    # Retrive the candidate by name
    if inputType == 'string':
        return ballot.getCandidateByName(selectedBallot, candidateId)

# Returns the type of a raw input ("integer" or "string")
def checkInputType(value):

    # Check if an integer was given
    try: int(value)
    except ValueError:
        # The input was a string
        return 'string'

    else:
        # The input was an integer
        return 'integer'
