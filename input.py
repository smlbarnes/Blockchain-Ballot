# Import custom modules
import output
import ballot
import keys

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
