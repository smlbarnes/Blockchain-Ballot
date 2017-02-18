# Import required modules
import os
import time

# Import custom modules
import file
import solidity
import geth
import crypto
import input

# Definition for a ballot
class Ballot:
    def __init__(self, title, address):

        # The local title of the ballot
        self.title = title

        # Address where the ballot is located
        self.address = address

# Save a ballot to file
def saveBallot(title, address):

    # Save the ballot to the file system
    file.save('ballots/' + title + '.ballot', address)

# Get a saved ballot by an index
def getBallotByIndex(index):

    # Get the ballots
    allBallots = savedBallots()

    # Return false if there is no ballot at the index
    if len(allBallots) <= index or index < 0:
        return False

    # Return the ballot at the index
    return allBallots[index]

# Get a saved ballot by it's name
def getBallotByName(name):

    # Get the ballots
    allBallots = savedBallots()

    # Loop through each saved ballot
    for index in xrange(len(allBallots)):

        # Return this ballot if the name matches
        if allBallots[index].title == title:
            return allBallots[index]

    # Loop completed, no ballot found with given name
    return False

# Get the index of a candidate by their name
def getCandidateByName(ballot, name):

    # Get the candidates
    candidates = getCandidates(ballot)

    # Loop through each candidate
    for index in xrange(len(candidates)):

        # Return this candidate if the name matches
        if candidates[index] == name:
            return index

    # Loop completed, no candidate found with given name
    return False

# Extract the details of a ballot from a file
def extractBallotFileData(ballotFile):

    # Create an array of values from the ballot file
    ballotFileArray = ballotFile.split(',')

    # Extract the ballot title
    ballotTitle = ballotFileArray[0]

    # Extract the ballot address
    ballotAddress = ballotFileArray[1]

    # Return the extracted data
    return ballotTitle, ballotAddress

# Import a ballot
def importBallot(filePath):

    # Read the ballot file at the given path
    ballotFile = file.read(filePath)

    # Get the data from the csv
    title, address = extractBallotFileData(ballotFile)

    # Save the ballot
    saveBallot(title, address)

# Export a ballot
def export(ballotToExport):

    # Add the ballot name to the export
    content = ballotToExport.title

    # Add the ballot address to the export
    content += "," + ballotToExport.address

    # Save the export
    file.save(ballotToExport.title + ' Export.csv', content)

# Get the saved ballots
def savedBallots():

    # Initalise the saved ballots array
    savedBallots = []

    # Loop through the directory for the saved ballots
    for fileName in os.listdir('ballots/'):

        # Check that it is a csv file
        if os.path.isfile('ballots/' + fileName) and fileName.endswith('.ballot'):

            # Deduce the ballot title from the filename
            title = fileName.replace('.ballot', '')

            # Get the ballot address from the file
            address = file.read('ballots/' + fileName)

            # Create a new saved ballot object and add it to the return array
            savedBallots.append(Ballot(title, address))

    # Return the array of saved ballots
    return savedBallots

# Delete a saved ballot
def delete(ballot):

    # Delete the ballot file
    file.delete('ballots/' + ballot.title + '.csv')

# Initalise a new ballot
def initalise(account, title, description, candidates, voters, key):

    # Initalise the public key 'n' chunks array
    publicKeyNChunks = []

    # Calculate the number of candidates
    candidatesCount = len(candidates)

    # Rebuild the candidates string
    candidatesString = ','.join(candidates)

    # Get the number of public key 'n' 256 bit chunks required
    nChunksLength = (key.publicKey.n.bit_length() / 256) + 1

    # Convert the public key 'n' into hexidecimal
    publicKeyNHex = geth.numberToHex(key.publicKey.n)

    # Loop through each 'n' chunk
    for index in xrange(nChunksLength):

        # Add this chunk to the array
        publicKeyNChunks.append(publicKeyNHex[index * 64 : (index + 1) * 64])

    # Initalise the public key 'g' chunks array
    publicKeyGChunks = []

    # Get the number of public key 'g' 256 bit chunks required
    gChunksLength = (key.publicKey.g.bit_length() / 256) + 1

    # Convert the public key 'g' into hexidecimal
    publicKeyGHex = geth.numberToHex(key.publicKey.g)

    # Loop through each 'g' chunk
    for index in xrange(gChunksLength):

        # Add this chunk to the array
        publicKeyGChunks.append(publicKeyGHex[index * 64 : (index + 1) * 64])

    # Convert the ballot arguments to hexidecimal format
    titleHex = geth.stringToHex(title)
    descriptionHex = geth.stringToHex(description)
    candidatesHex = geth.stringToHex(candidatesString)
    candidatesCountHex = geth.numberToHex(candidatesCount)

    # Get the length of the ballot arguments and convert to hex
    # Characters for strings, array size for arrays
    titleLengthHex = geth.numberToHex(len(title))
    descriptionLengthHex = geth.numberToHex(len(description))
    candidatesLengthHex = geth.numberToHex(len(candidatesString))
    votersLengthHex = geth.numberToHex(len(voters))
    publicKeyNChunksLengthHex = geth.numberToHex(len(publicKeyNChunks))
    publicKeyGChunksLengthHex = geth.numberToHex(len(publicKeyGChunks))

    # Compile the ballot contract
    compiledBallot = solidity.compile('contracts/ballot.sol').itervalues().next()

    # Extract the ballot contract ABI (Application Binary Interface)
    contractAbi = compiledBallot['abi']

    # Initalise the ballot creation bytecode
    ballotCreationCode = ""

    # Add the contract bytecode
    ballotCreationCode += compiledBallot['code']

    # Declare the number of arguments (for use in calculating offsets)
    ballotArguments = 7

    # Add the offset for the title argument
    ballotCreationCode += geth.pad(geth.numberToHex(ballotArguments * 32))

    # Add the offset for the description argument
    ballotCreationCode += geth.pad(geth.numberToHex((2 + (len(titleHex) / 64) + ballotArguments) * 32))

    # Add the offset for the candidates argument
    ballotCreationCode += geth.pad(geth.numberToHex((2 + (len(titleHex) / 64) + 2 + (len(descriptionHex) / 64) + ballotArguments) * 32))

    # Add the candidates count argument
    ballotCreationCode += geth.pad(candidatesCountHex)

    # Add the offset for the voters argument
    ballotCreationCode += geth.pad(geth.numberToHex((2 + (len(titleHex) / 64) + 2 + (len(descriptionHex) / 64) + 2 + (len(candidatesHex) / 64) + (len(candidatesCountHex) / 64) + ballotArguments) * 32))

    # Add the offset for the public key 'n' argument
    ballotCreationCode += geth.pad(geth.numberToHex((2 + (len(titleHex) / 64) + 2 + (len(descriptionHex) / 64) + 2 + (len(candidatesHex) / 64) + 1 + (len(candidatesCountHex) / 64) + (len(voters)) + ballotArguments) * 32))

    # Add the offset for the public key 'g' argument
    ballotCreationCode += geth.pad(geth.numberToHex((2 + (len(titleHex) / 64) + 2 + (len(descriptionHex) / 64) + 2 + (len(candidatesHex) / 64) + 2 + (len(candidatesCountHex) / 64) + (len(voters)) + len(publicKeyNChunks) + ballotArguments) * 32))

    # Add the ballot title
    ballotCreationCode += geth.pad(titleLengthHex)
    ballotCreationCode += geth.pad(titleHex, 'left')

    # Add the ballot description
    ballotCreationCode += geth.pad(descriptionLengthHex)
    ballotCreationCode += geth.pad(descriptionHex, 'left')

    # Add the ballot candidates
    ballotCreationCode += geth.pad(candidatesLengthHex)
    ballotCreationCode += geth.pad(candidatesHex, 'left')

    # Add the ballot voters
    ballotCreationCode += geth.pad(votersLengthHex)
    for index in xrange(len(voters)):
        ballotCreationCode += geth.pad(voters[index])

    # Add the ballot public key
    ballotCreationCode += geth.pad(publicKeyNChunksLengthHex)
    for index in xrange(len(publicKeyNChunks)):
        ballotCreationCode += geth.pad(publicKeyNChunks[index])
    ballotCreationCode += geth.pad(publicKeyGChunksLengthHex)
    for index in xrange(len(publicKeyGChunks)):
        ballotCreationCode += geth.pad(publicKeyGChunks[index])

    # Deploy the ballot contract
    contractTransactionHash = geth.deployContract(account, ballotCreationCode)

    # Check if there was an error sending the transaction
    if('error' in contractTransactionHash):

        # Output the error and abort the ballot
        print 'Error deploying contract: "' + contractTransactionHash['error']['message'] + '"'

    else:

        # Loop to wait until a transaction is confirmed
        print 'Waiting for contract to deploy...'
        while True:

            # Wait 1 seconds before rechecking for a transaction receipt
            time.sleep(1)

        	# Attempt to get the transaction receipt for the deployed contract
            transactionReceipt = geth.getTransactionReceipt(contractTransactionHash)['result']

        	# Check if a receipt is available
            if transactionReceipt is not None:

        		# The transaction has been mined, break the loop
                break

        # Get the contract address from the receipt
        contractAddress = transactionReceipt['contractAddress']

        # Save the ballot
        saveBallot(title, contractAddress)

        # Return control to the program
        print 'Ballot contract deployed.'

# Attempt to vote in a ballot
def executeVote(ballotAddress, account, vote):

    # Initalise the sendable votes
    sendableVotes = []

    # Loop through each 2056 bit vote value
    for voteIndex in xrange(len(vote)):

        # Convert the value to hex
        voteHex = geth.numberToHex(vote[voteIndex])

        # Get the length of the hex
        hexLength = len(str(voteHex))

        # Check if the hex is less than 512
        if hexLength < 512:

            # Get how much to pad the first value by
            paddingRequired = 512 - hexLength

            # Split the vote value into sendable 256 bit chunks
            for index in xrange(8):

                # Check if this is the first chunk
                if index == 0:

                    # Add this 256 bit chunk
                    sendableVotes.append(voteHex[64*index:64*(index + 1)-paddingRequired])

                else:

                    # Add this 256 bit chunk
                    sendableVotes.append(voteHex[64*index-paddingRequired:64*(index + 1)-paddingRequired])

        else:

            # Split the vote value into sendable 256 bit chunks
            for index in xrange(8):

                # Add this 256 bit chunk
                sendableVotes.append(voteHex[64*index:64*(index + 1)])

    # Initalise the vote bytecode with the offset
    voteBytecode = geth.pad(geth.numberToHex(32))

    # Add the vote array length
    voteBytecode += geth.pad(geth.numberToHex(len(sendableVotes)))

    # Loop through each 256 bit chunk of the sendable vote
    for index in xrange(len(sendableVotes)):

        # Add this chunk to the sendable bytecode
        voteBytecode += geth.pad(sendableVotes[index])

    # Attempt the vote transaction
    voteTransactionHash = geth.castVote(ballotAddress, account, voteBytecode)

    # Check if there was an error sending the transaction
    if('error' in voteTransactionHash):

        # Output the error and abort the ballot
        print 'Error deploying contract: "' + voteTransactionHash['error']['message'] + '"'

    else:

        # Loop to wait until a transaction is confirmed
        print 'Waiting for vote to send...'
        while True:

            # Wait 1 seconds before rechecking for a transaction receipt
            time.sleep(1)

        	# Attempt to get the transaction receipt for the deployed contract
            transactionReceipt = geth.getTransactionReceipt(voteTransactionHash)['result']

        	# Check if a receipt is available
            if transactionReceipt is not None:

        		# The transaction has been mined, break the loop
                break

# Build a vote for a ballot
def buildVote(ballot, candidateIndex):

    # Get the ballots public key
    publicKey = getPublicKey(ballot)

    # Initalise the vote
    vote = []

    # Loop through each candidate in the ballot
    for index in xrange(len(getCandidates(ballot))):


        # Check if this is the candidate to vote for
        if (index == candidateIndex):

            # Add a positive value to the vote
            value = crypto.encrypt(publicKey, 1)
            vote.append(value)

        else:

            # Add a negative value to the vote
            value = crypto.encrypt(publicKey, 0)
            vote.append(value)

    # Return the encrypted vote
    return vote

# Get a ballots title
def getTitle(ballot):
    titleResponse = geth.callFunction(ballot.address, 'getTitle')['result']
    return geth.responseToString(titleResponse)

# Get a ballots description
def getDescription(ballot):
    descriptionResponse = geth.callFunction(ballot.address, 'getDescription')['result']
    return geth.responseToString(descriptionResponse)

# Get a ballots candidates
def getCandidates(ballot):
    candidatesResponse = geth.callFunction(ballot.address, 'getCandidates')['result']
    return geth.responseToCandidates(candidatesResponse)

# Get a ballots candidate count
def getCandidateCount(ballot):
    candidateCountResponse = geth.callFunction(ballot.address, 'getCandidateCount')['result']
    return geth.responseToInteger(candidateCountResponse)

# Get a ballots voters
def getVoters(ballot):
    votersResponse = geth.callFunction(ballot.address, 'getVoters')['result']
    return geth.responseToVoters(votersResponse)

# Get a ballots public key
def getPublicKey(ballot):

    # Get the public key 'n'
    publicKeyResponse = geth.callFunction(ballot.address, 'getPublicKeyN')['result']
    publicKeyN = geth.responseToPublicKey(publicKeyResponse)

    # Get the public key 'g'
    publicKeyResponse = geth.callFunction(ballot.address, 'getPublicKeyG')['result']
    publicKeyG = geth.responseToPublicKey(publicKeyResponse)

    # Return a public key object
    return crypto.PublicKey(publicKeyN, publicKeyG)

# Get a ballots votes
def getVotes(ballot):

    # Get the vote values for the selected ballot
    votesResponse = geth.callFunction(ballot.address, 'getVotes')['result']
    voteValues = geth.responseToVoteValues(votesResponse)

    # Get the candidate count
    candidateCount = getCandidateCount(ballot)

    # Initalise the votes array
    votes = []

    # Loop through each set of votes
    for index in xrange((len(voteValues) / 8) / candidateCount):

        # Add a row for this set of votes
        votes.append([])

        # Loop through each candidate
        for candidateIndex in xrange(candidateCount):

            # Initalise this vote value
            voteValue = ''

            # Loop through each value for this candidate
            for valueIndex in xrange(8):

                # Compile this vote
                voteValue += str(voteValues[((index * (candidateCount * 8)) + (candidateIndex) * 8) + valueIndex])

            # Add the vote value to the vote array
            votes[index].append(geth.hexToNumber(voteValue))

    # Return the votes array
    return votes