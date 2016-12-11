# Import custom modules
import ballot
import keys

# Output a list of all the saved ballots
def allBallots(showIndexes=False, showBallotDetail=True):

    # Get the saved ballots
    savedBallots = ballot.savedBallots();

    # Check if there are any saved ballots
    if len(savedBallots) < 1:

        # No saved ballots where found
        print "No ballots found."

    else:

        # Loop through each saved ballot
        for index in xrange(len(savedBallots)):

            # Initalise this ballots output
            output = ''

            # Check if an index needs to be added
            if showIndexes:

                # Add the index of the saved ballot
                output += str(index + 1) + ' - '

            # Add the title of the ballot
            output += savedBallots[index].title

            # Check if details about the ballot are to be shown
            if showBallotDetail:

                # Add the ballots address
                output += ' - Address: ' + savedBallots[index].address

            # Output the ballot
            print output

# Output a list of all the saved keys
def allKeys(showIndexes=False, showKeyDetail=True):

    # Get the saved keys
    savedKeys = keys.savedKeys();

    # Check if there are any saved keys
    if len(savedKeys) < 1:

        # No saved keys where found
        print "No keys found."

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
