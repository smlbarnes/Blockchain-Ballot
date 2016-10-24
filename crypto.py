# Import required modules
import sys
import random

# Definition for a public key
class PublicKey:
    def __init__(self, n, e):
        # 'n' is a product of the two primes chosen for the key
        self.n = n

        # 'e' is the public exponent used to encrypt messages
        self.e = e

# Definition for a private key
class PrivateKey:
    def __init__(self, n, d):
        # 'n' is a product of the two primes chosen for the key
        self.n = n

        # 'd' is the modular inverse of e mod phi(n)
        self.d = d

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

# Calculate modular inverse (a^-1 mod c)
def modularInverse(a, c):

    # Set 'b' as 'c' for use in the algorithm
    b = c

    # Set initial Bezout Coefficients
    coefficientT = 0
    lastCoefficientT = 1
    coefficientS = 1
    lastCoefficientS = 0

    # Loop until a GCD is found
    gcdFound = False
    while not gcdFound:

        # Calculate the quotient for this round
        quotient = a // b

        # Calculate the remainder for this round
        a, b = b, a % b

        # Check if the GCD has been found
        if (b == 0):
            gcdFound = True

        # Calculate the coefficients for this round
        coefficientT, lastCoefficientT = lastCoefficientT - quotient * coefficientT, coefficientT
        coefficientS, lastCoefficientS = lastCoefficientS - quotient * coefficientS, coefficientS

    # Return the calculated inverse
    return lastCoefficientT % c

# Encrypt plaintext using a public key
def encrypt(publicKey, plaintext):
    cyphertext = pow(plaintext, publicKey.e, publicKey.n)
    return cyphertext

# Decrypt cyphertext using a private key
def decrypt(privateKey, cyphertext):
    plaintext = pow(cyphertext, privateKey.d, privateKey.n)
    return plaintext

# Generate an RSA private key and related public key
def generateRSAKeyPair():

    # Get 2 RSA suitable prime numbers
    firstPrime = generateRSAPrime()
    secondPrime = generateRSAPrime()

    # Ensure the primes are distinct
    if firstPrime == secondPrime:

        # Reattempt the generation
        return generateRSAKeyPair()

    # Compute composite number 'n'
    n = firstPrime * secondPrime

    # Compute the phi of 'n'
    phiN = (firstPrime - 1) * (secondPrime - 1)

    # Compute a coprime of 'phiN', 'e' where 1 < e < phiN
    eFound = False
    while not eFound:
        e = random.randrange(2, phiN)
        if isProbablePrime(e) and e % phiN != 0:
            eFound = True

    # Compute 'd', the modular inverse of 'e' 'phiN', d = e^-1 mod phiN
    d = modularInverse(e, phiN)

    # Create the public key
    public = PublicKey(n, e)

    # Create the private key
    private = PrivateKey(n, d)

    # Return the key pair
    return public, private
