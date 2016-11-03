# Initalise a new ballot
def initalise():

    # Get the name of the ballot
    title = raw_input("Title of the ballot: ")

    # Get the description of the ballot
    description = raw_input("Description for the ballot: ")

    # Get the ballot candidates
    candidatesString = raw_input("Please enter the candidates separated by commas (','): ")
    candidates = candidatesString.split(",")

    # Get the voter addresses
    votersString = raw_input("Please enter the voter addresses separated by commas (','): ")
    voters = candidatesString.split(",")

    # Get the ballot public key
    publicKey = raw_input("Enter the public key of the ballot: ")

    #TODO Implement the rest of this
