# Import custom modules
import keys

# Output a list of all the saved keys
def allKeys(showIndexes=False, showKeyDetail=True):

    # Get the saved keys
    savedKeys = keys.savedKeys();

    # Check if there are any saved keys
    if len(savedKeys) < 1:

        # No saved keys where found
        print "No saved keys found."

    else:

        # Loop through each saved key
        for index in xrange(len(savedKeys)):

            # Initalise this keys output
            output = ''

            # Check if an index needs to be added
            if showIndexes:

                # Add the index of the saved key
                output += str(index + 1) + ' - '

            # Add the name of the key
            output += savedKeys[index].name

            # Check if details about the key are to be shown
            if showKeyDetail:

                # Check if the key has a private key
                if savedKeys[index].privateKey:

                    # The key has both
                    output += ' - Public and Private'

                else:

                    # The key is public only
                    output += ' - Public Only'

            # Output the key
            print output
