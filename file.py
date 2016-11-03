import os

# Definition for a saved key
class SavedKey:
    def __init__(self, name, hasPrivate):

        # Name assigned to the key
        self.name = name

        # Whether the private key is saved
        self.hasPrivate = hasPrivate

# Get details on the saved keys
def getSavedKeys():

    # Initalise the saved key array
    savedKeys = []

    # Loop through the directory for the public keys
    for file in os.listdir('keys/public/'):

        # Check that it is a csv file
        if os.path.isfile('keys/public/' + file) and file.endswith('.csv'):

            # Deduce the name of the key from the filename
            name = file.replace('.csv', '')

            # Check if a corresponding private key exists and set the flag
            if os.path.isfile('keys/private/' + file):
                hasPrivate = True
            else:
                hasPrivate = False

            # Create a new saved key object and add it to the return array
            savedKeys.append(SavedKey(name, hasPrivate))

    # Return the array of saved keys
    return savedKeys

# Save a key to the file system
def saveKey(keyName, publicKey, PrivateKey=False):

    # Convert the public key object into an array
    publicKeyArray = [publicKey.n, publicKey.g]

    # Save the public key to the file system
    saveFile('keys/public/' + keyName + '.csv', arrayToCsv(publicKeyArray))

    # Check if a private key was given
    if PrivateKey:

        # Convert the private key object into an array
        privateKeyArray = [PrivateKey.n, PrivateKey.phiN, PrivateKey.u]

        # Save the privte key to the file system
        saveFile('keys/private/' + keyName + '.csv', arrayToCsv(privateKeyArray))

# Import a key
def importKey():

    # Get the file path for the public key
    publicKeyPath = raw_input("Please give the path to the key file: ")
    print ''

    # Attempt to import the key

# Export a key
def exportKey():

    # Get the saved keys
    savedKeys = getSavedKeys();

    # Check if there are any saved keys
    if len(savedKeys) < 1:

        # No saved keys where found
        print "You don't have any keys to export."

    else:

        # Loop through each saved key
        for index in xrange(len(savedKeys)):

            # Add the index of the saved key
            output = str(index + 1) + ' - '

            # Add the name of the key
            output += savedKeys[index].name + ' - '

            # Check if the key has a private key
            if savedKeys[index].hasPrivate:

                # The key has both
                output += ' Public and Private'

            else:

                # The key is public only
                output += ' Public Only'

            # Display the information about this key
            print output

    # Ask the user which key they want to export
    print ''
    keyId = raw_input("Please enter the name or the number of the key you want to export: ")
    print ''

    # Set the selected key flag incase the key to export cannot be found
    selectedKey = False

    # Check if an index was given
    try:
        int(keyId)
    except ValueError:
        # Set the flag for a name
        indexGiven = False
    else:
        # Set the flag for an index
        indexGiven = True

    # Check if an index was given
    if indexGiven:

        # Get the key by it's index
        selectedKey = savedKeys[int(keyId) - 1]

    else:

        # Loop through each saved key
        for index in xrange(len(savedKeys)):

            # Check if this is the right key
            if savedKeys[index].name == keyId:

                # This is the key to export
                selectedKey = savedKeys[index]

    # Check that the selected key was found
    if not selectedKey:

        # Display an error
        print 'Sorry the key "' + keyId + '''" wasn't found, did you type the name correctly?'''

    else:

        #
        print 'lala'

# Write to the file system
def saveFile(filePath, content):

    # Open a file at the given path
    file = open(filePath, 'w')

    # Write the content to the file
    file.write(content)

    # Close the file
    file.close()

# Convert an array to a csv
def arrayToCsv(array, csv=""):

    # Loop through the array
    for index in range(len(array)):

        # TODO Only add trailing comma to values that need it

        # Append the array element to the csv
        csv += ',' + str(array[index])

    # Return the completed csv
    return csv
