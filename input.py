# Import custom modules
import output
import keys

# Get a saved key of the user's choice
def getKeySelection():

    # Show a list of all keys with indexes
    output.allKeys(True)

    # Ask the user which key they want to export
    print ''
    keyId = raw_input("Please enter the name or number of the key you want to export: ")

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
