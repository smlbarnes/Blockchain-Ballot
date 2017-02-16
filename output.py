# Import custom modules
import ballot
import keys
import geth

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

# Output a list of all available Ethereum accounts
def allAccounts(showIndexes=False, showAccountDetail=True):

    # Get the accounts from the geth instance
    accounts = geth.accounts()

    # Check if there are any accounts
    if len(accounts) < 1:

        # No accounts where found
        print "No accounts found."

    else:

        # Loop through each account
        for index in xrange(len(accounts)):

            # Initalise this accounts output
            output = ''

            # Check if an index needs to be added
            if showIndexes:

                # Add the index of the account
                output += str(index + 1) + ' - '

            # Add the address of the account
            output += accounts[index]

            # Check if details about the account are to be shown
            if showAccountDetail:

                # Add the balance of the account
                output += " | " + str(geth.getBalance(accounts[index])) + " Ether"

            # Output the key
            print output

# Output the information of a ballot
def ballotInfo(targetBallot, showCandidates=True, showVoters=True):

    # Get the ballot title
    title = ballot.getTitle(targetBallot)

    # Get the ballot description
    description = ballot.getDescription(targetBallot)

    # Display the ballot information
    print ''
    print title
    print description

    # Check if the candidates should be shown
    if (showCandidates):

        # Get the ballot candidates
        candidates = ballot.getCandidates(targetBallot)

        # Display the candidates
        print ''
        print 'Candidates:'
        for candidate in candidates: print candidate

    # Check if the voters should be shown
    if (showVoters):

        # Get the ballot voters
        voters = ballot.getVoters(targetBallot)

        # Display the voters
        print ''
        print 'Voters:'
        for voter in voters: print voter

# Output the candidates of a ballot
def candidates(targetBallot, showIndexes=True):

    # Get the ballot candidates
    candidates = ballot.getCandidates(targetBallot)

    # Loop through each candidate
    for index in xrange(len(candidates)):

        # Initalise this candidates output
        output = ''

        # Check if an index needs to be added
        if showIndexes:

            # Add the index of the candidate
            output += str(index + 1) + ' - '

        # Add the name of the candidate
        output += candidates[index]

        # Output the candidate
        print output