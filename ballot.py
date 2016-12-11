# Import required modules
import os

# Import custom modules
import file

# Definition for a ballot
class Ballot:
    def __init__(self, title, address):

        # The local title of the ballot
        self.title = title

        # Address where the ballot is located
        self.address = address

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

# Get the saved ballots
def savedBallots():

    # Initalise the saved ballots array
    savedBallots = []

    # Loop through the directory for the saved ballots
    for fileName in os.listdir('ballots/'):

        # Check that it is a csv file
        if os.path.isfile('ballots/' + fileName) and fileName.endswith('.csv'):

            # Deduce the ballot title from the filename
            title = fileName.replace('.csv', '')

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

#TODO Initalise a new ballot
def initalise(title, description, candidates, voters, deadline, publicKey):

    # Initalise the ballot object
    newBallot = Ballot(title, description, candidates, voters, deadline, publicKey)

    print 'TODO initalise ballot'
