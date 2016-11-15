# Import required modules
import sys
import random

# Import custom modules
import file

# Definition for a public key
class PublicKey:
    def __init__(self, n, g):

        # 'n' is a product of the two primes chosen for the key
        self.n = n

        # 'g' is the public exponent used to encrypt messages
        self.g = g

# Definition for a private key
class PrivateKey:
    def __init__(self, n, phiN, u):

        # 'n' is a product of the two primes chosen for the key
        self.n = n

        # 'phiN' is the phi of the two primes chosen for the key
        self.phiN = phiN

        # 'u' is the modular inverse of e mod phi(n)
        self.u = u

# Generate a random number of 'n' bits from the system entropy function
def randomNumber(bits):
    return random.SystemRandom().getrandbits(bits)

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

# Generate a probable prime suitable for use in public key encryption
def generatePrime():

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

# Generate a Paillier private key and related public key
def generateKeyPair():

    # Get 2 Paillier suitable prime numbers
    firstPrime = generatePrime()
    secondPrime = generatePrime()

    # Ensure the primes are distinct
    if firstPrime == secondPrime:

        # Reattempt the generation
        return generateKeyPair()

    # Compute composite number 'n'
    n = firstPrime * secondPrime

    # Compute the phi of 'n'
    phiN = (firstPrime - 1) * (secondPrime - 1)

    # Compute 'g' for the public key
    g = n + 1

    # Compute the modular inverse of 'phiN' 'n', phiN^-1 mod n
    u = modularInverse(phiN, n)

    # Create the public key
    public = PublicKey(n, g)

    # Create the private key
    private = PrivateKey(n, phiN, u)

    # Return the key pair
    return public, private

# Encrypt plaintext using a Paillier public key
def encrypt(publicKey, plaintext):

    # Calculate n^2
    nSquared = publicKey.n ** 2

    # Generate a random 'r' where 1 < r < n
    r = random.randrange(2, publicKey.n)

    # Compute the cyphertext as cyphertext = (g^plaintext mod n^2) * (r^n mod n^2) mod n^2
    cyphertext = ( pow(publicKey.g, plaintext, nSquared) *
                   pow(r, publicKey.n, nSquared) % nSquared )

    # Return the encrypted cypher
    return cyphertext

# Decrypt Paillier cyphertext using a private key
def decrypt(privateKey, cyphertext):

    # Calculate n^2
    nSquared = privateKey.n ** 2

    # Compute the plaintext as plaintext = L(cyphertext^phiN mod n^2) * u mod n
    # Where L(x) = (x - 1) / n
    plaintext = ( (pow(cyphertext, privateKey.phiN, nSquared) - 1)
                   // privateKey.n * privateKey.u % privateKey.n )

    # Return the decrypted plaintext
    return plaintext

# Apply a homomorphic addition to two integers encrypted by the same key
def homomorphicAdd(publicKey, encryptedInteger1, encryptedInteger2):

    # Compute the addition as result = encryptedInteger1 * encryptedInteger2 mod n^2
    return encryptedInteger1 * encryptedInteger2 % (publicKey.n ** 2)
