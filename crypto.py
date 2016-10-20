# Import required modules
import sys
import random

# Perform an 'n' round Miller-Rabin primality test (default 40 rounds has fault rate of 2^-128)
def millerRabin(number, rounds=40):

    # Get 'm' and 'k' that satisfies 'number - 1 = 2^k * m' with whole numbers
    # Initalise 'k'
    k = 0

    # Initalise 'm'
    m = number - 1

    # When 'm' becomes odd the next iteration wont be whole
    while m % 2 == 0:

        # Iterate 'k'
        k += 1

        # Calculate 'm'
        m /= 2

    # Perform the specified number of rounds
    for index in xrange(rounds):

        # Perform a single round
        if not millerRabinRound(number, m, k):

            # The round failed, the number is a composite
            return False

        # The number passed the specified rounds of accuracy
        return True

# Perform a single Miller-Rabin round for the given values
# Returns true for a round pass
def millerRabinRound(number, m, k):

    # Generate a random 'a' where 1 < a < number - 1
    a = random.randrange(2, number - 1)

    # Calculate the value for 'x' where x = a^m mod number
    x = pow(a, m, number)

    # Check if 'x' is 1 or 'number' - 1 which indicates a probable prime
    if x == 1 or x == number - 1:

        # The number has passed the round
        return True

    # Loop the operation 'k' times until a round pass or a composite is found
    for index in xrange(k - 1):

        # Recalculate 'x'
        x = pow(x, 2, number)

        # Break loop if 'x' is 'number' - 1
        if x == number - 1:
            break

    # If the loop completes the number is composite
    else:

        # The number has failed the round
        return False

    #The number has passed the round
    return True


# Test if a number is a probable prime
def isProbablePrime(number):

    # Number is not prime if it is even
    if number % 2 == 0:
        return False

    # Perform a Miller-Rabin test with the default number of rounds
    if millerRabin(number):

        # The number passed the test
        return True

    else:

        # The number failed the test
        return False

# Generate a random number of 'n' bits from the system entropy function
def randomNumber(bits):
    return random.SystemRandom().getrandbits(bits)

# Generate a probable prime suitable for use in RSA
def generateRSAPrime():

    # Loop until a suitable prime is found
    while True:

        # Generate a number of 512 bits
        possiblePrime = randomNumber(512)

        # Return the number if it is a probable prime
        if isProbablePrime(possiblePrime):
            return possiblePrime
