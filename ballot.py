# Initalise a new ballot
def initalise():

    # Get the name of the ballot
    title = raw_input("Title of the ballot: ")
    print ''

    # Get the description of the ballot
    description = raw_input("Description for the ballot: ")
    print ''

    # Get the ballot candidates
    candidatesString = raw_input("Please enter the candidates separated by commas (','): ")
    candidates = candidatesString.split(",")
    print ''

    # Get the voter addresses
    votersString = raw_input("Please enter the voter addresses separated by commas (','): ")
    voters = candidatesString.split(",")
    print ''

    # Get the ballot public key
    publicKey = raw_input("Enter the public key of the ballot: ")
    print ''

    #TODO Implement the rest of this
