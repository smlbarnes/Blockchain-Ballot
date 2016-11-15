# Import required modules
import os

# Import custom modules
import file
import crypto

# Definition for a saved key
class SavedKey:
    def __init__(self, name, publicKey, privateKey=False):

        # Name assigned to the key
        self.name = name

        # The public key
        self.publicKey = publicKey

        # Path to the public key
        self.publicKeyFile = 'keys/public/' + name + '.csv'

        # Check whether a corresponding public key was given
        if privateKey == False:

            # Set negative flags for the private key vlaues
            self.privateKey = False
            self.privateKeyFile = False

        else:

            # The private key
            self.privateKey = privateKey

            # Path to the public key
            self.privateKeyFile = 'keys/private/' + name + '.csv'

# Get a saved key by an index
def getKeyByIndex(index):

    # Get the keys
    allKeys = savedKeys()

    # Return false if there is no key at the index
    if len(allKeys) <= index or index < 0:
        return False

    # Return the key at the index
    return allKeys[index]

# Get a saved key by it's name
def getKeyByName(name):

    # Get the keys
    allKeys = savedKeys()

    # Loop through each saved key
    for index in xrange(len(allKeys)):

        # Return this key if the name matches
        if allKeys[index].name == name:
            return allKeys[index]

    # Loop completed, no key found with given name
    return False

# Get details on the saved keys
def savedKeys():

    # Initalise the saved key array
    savedKeys = []

    # Loop through the directory for the public keys
    for fileName in os.listdir('keys/public/'):

        # Check that it is a csv file
        if os.path.isfile('keys/public/' + fileName) and fileName.endswith('.csv'):

            # Deduce the name of the key from the filename
            name = fileName.replace('.csv', '')

            # Set the public key file path
            publicKeyFile = 'keys/public/'+ name + '.csv'

            # Read the public key file
            publicKeyFileContents = file.read(publicKeyFile)

            # Split the file into an array of values
            publicKeyFileValues = publicKeyFileContents.split(',')

            # Set the public key
            publicKey = crypto.PublicKey(publicKeyFileValues[0], publicKeyFileValues[1])

            # Check if a corresponding private key exists and set the flag
            if os.path.isfile('keys/private/' + fileName):

                # Set the private key file path
                privateKeyFile = 'keys/private/'+ name + '.csv'

                # Read the private key file
                privateKeyFileContents = file.read(privateKeyFile)

                # Split the file into an array of values
                privateKeyFileValues = privateKeyFileContents.split(',')

                # Set the private key
                privateKey = crypto.PrivateKey(privateKeyFileValues[0], privateKeyFileValues[1], privateKeyFileValues[2])

                # Create a new saved key object with the private key and add it to the return array
                savedKeys.append(SavedKey(name, publicKey, privateKey))

            else:

                # Create a new saved key object without the private key and add it to the return array
                savedKeys.append(SavedKey(name, publicKey))

    # Return the array of saved keys
    return savedKeys

# Save a key to the file system
def saveKey(keyName, publicKey, privateKey=False):

    # Convert the public key object into an array
    publicKeyArray = [publicKey.n, publicKey.g]

    # Save the public key to the file system
    file.save('keys/public/' + keyName + '.csv', file.arrayToCsv(publicKeyArray))

    # Check if a private key was given
    if privateKey:

        # Convert the private key object into an array
        privateKeyArray = [privateKey.n, privateKey.phiN, privateKey.u]

        # Save the privte key to the file system
        file.save('keys/private/' + keyName + '.csv', file.arrayToCsv(privateKeyArray))

# Extract the key data from a key file
def extractKeyFileData(keyFile):

    # Create an array of values from the key file
    keyFileArray = keyFile.split(',')

    # Extract the key name
    keyName = keyFileArray[0]

    # Create a new public key
    publicKey = crypto.PublicKey(keyFileArray[1], keyFileArray[2])

    # Check if there is a private key
    if len(keyFileArray) > 3:

        # Create a new private key
        privateKey = crypto.PrivateKey(keyFileArray[3], keyFileArray[4], keyFileArray[5])

    else:

        # No private key in file
        privateKey = False

    # Return the extracted data
    return keyName, publicKey, privateKey

# Import a key
def importKey(filePath):

    # Read the key file at the given path
    keyCsv = file.read(filePath)

    # Get the data from the csv
    keyName, publicKey, privateKey = extractKeyFileData(keyCsv)

    # Save the key
    saveKey(keyName, publicKey, privateKey)

# Export a key
def export(key, includePrivateKey=True):

    # Add the key name to the export
    content = key.name

    # Add the public key to the export
    content += "," + file.read('keys/public/' + key.name + '.csv')

    # Check if there is a corresponding private key and the user wanted to include it
    if includePrivateKey:

        # Add the private key to the export
        content += "," + file.read('keys/private/' + key.name + '.csv')

    # Save the export
    file.save(key.name + ' Export.csv', content)

# Delete a saved key
def delete(key):

    # Delete the public key file
    file.delete(key.publicKeyFile)

    # Check if there is a private key
    if key.privateKey:

        # Delete the private key file
        file.delete(key.privateKeyFile)

# Returns whether a key exists (specified by name or index)
def keyExists(keyId):

    # Get the saved keys
    savedKeys = savedKeys();

    # Check if a name or index was given
    if checkInputType(keyId) == 'integer':

        # Check that a key exists at the index
        if int(keyId) > -1 and len(savedKeys) <= int(keyId):

            # A key exists at that index
            return True

        else:

            # No key exists at that index
            return False

    else:

        # Loop through each saved key
        for index in xrange(len(savedKeys)):

            # Check if this key has a matching name
            if savedKeys[index].name == keyId:

                # A key with the given name exists
                return True

        # No matching names where found
        return False
