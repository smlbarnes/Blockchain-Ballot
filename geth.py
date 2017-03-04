# Import required modules
import requests
import json
from sha3 import sha3_256

# Declare the location of the geth rpc
gethUrl = 'http://localhost:8080'

# Performs a request to the geth rpc
def rpcRequest(method, data, headers):

    # Attempt to use the geth rpc
    try:
        response = requests.request(method, gethUrl, json=data, headers=headers)

        # Return the response as an object
        return json.loads(response.content)

    # Handle a connection error
    except requests.ConnectionError:

        # Cannot connect return false
        return False

# The ballot contract abi
def abi():
    return {
        'getTitle': 'title()',
        'getDescription': 'description()',
        'getCandidates': 'candidates()',
        'getCandidateCount': 'candidatesCount()',
        'getVoters': 'getVoters()',
        'getPublicKeyN': 'getPublicKeyN()',
        'getPublicKeyG': 'getPublicKeyG()',
        'executeVote': 'executeVote(uint256[])',
        'getVotes': 'getVotes()'
    };

# Get the method id for a ballot function
def methodId(functionName):
    return "0x" + sha3_256(abi()[functionName]).hexdigest()[:8]

# Returns the accounts in the local geth instance
def accounts():

    # Define the request
    method = 'POST'
    data = {"jsonrpc": "2.0", "method": "eth_accounts", "params": [], "id": 1}
    headers = ''

    # Attempt the request
    response = rpcRequest(method, data, headers)

    # Return the list of accounts
    return response['result']

# Returns the balance of an address
def getBalance(address):

    # Define the request
    method = 'POST'
    data = {'jsonrpc': '2.0', 'method': 'eth_getBalance', 'params': [address, 'latest'], 'id': 1}
    headers = ''

    # Attempt the request
    response = rpcRequest(method, data, headers)

    # Return the balance in ether
    return weiToEther(hexToNumber(response['result']))

# Deploys a compiled contract to a random address
def deployContract(account, bytecode):

    # Define the request
    method = 'POST'
    data = {'jsonrpc': '2.0', 'method': 'eth_sendTransaction', 'params': [{'from': account, 'gas': '0x2000000', 'data': bytecode}], 'id': 1}
    headers = ''

    # Attempt the request
    response = rpcRequest(method, data, headers)

    # Check the response for errors
    if('error' in response):

        # Return the response
        return response

    # Return the transaction hash
    return response['result']

# Attempts to cast a vote in a ballot
def castVote(selectedBallot, account, bytecode):

    # Get the function signiture
    functionSigniture = methodId('executeVote')

    # Define the request
    method = 'POST'
    data = {'jsonrpc': '2.0', 'method': 'eth_sendTransaction', 'params': [{'from': account, 'to': selectedBallot.address, 'gas': '0x4000000', 'data': functionSigniture + bytecode}], 'id': 1}
    headers = ''

    # Attempt the request
    response = rpcRequest(method, data, headers)

    # Check the response for errors
    if('error' in response):

        # Return the response
        return response

    # Return the transaction hash
    return response['result']

# Get the transaction receipt from a hash
def getTransactionReceipt(hash):

    # Define the request
    method = 'POST'
    data = {'jsonrpc': '2.0', 'method': 'eth_getTransactionReceipt', 'params': [hash], 'id': 1}
    headers = ''

    # Attempt the request
    response = rpcRequest(method, data, headers)

    return response

# Call ballot function
def callFunction(ballotAddress, functionName):

    # Get the function signiture
    functionSigniture = methodId(functionName)

    # Define the request
    method = 'POST'
    data = {'jsonrpc': '2.0', 'method': 'eth_call', 'params': [{'to': ballotAddress, 'data': functionSigniture}, 'latest'], 'id': 1}
    headers = ''

    # Attempt the request
    response = rpcRequest(method, data, headers)

    return response

# Tests if geth is running with rpc enabled
def rpcRunning():

    # Define the request
    method = 'POST'
    data = {'jsonrpc': '2.0', 'method': 'web3_clientVersion', 'id': 1}
    headers = ''

    # Attempt the request
    response = rpcRequest(method, data, headers)

    # Check if the request could be performed
    if response:
        # Response was given geth rpc is running
        return True
    else:
        # Could not connect geth rpc is not running
        return False

# Encode a string into hex
def stringToHex(stringToConvert):
    return stringToConvert.encode('hex')

# Decode a string from hex
def hexToString(hexidecimal):
    return hexidecimal.decode('hex')

# Encode a denary number into hex
def numberToHex(integer):
    return hex(integer).rstrip("L").lstrip("0x")

# Decode a hexidecimal number to denary format
def hexToNumber(hexidecimal):
    return int(hexidecimal, 16)

# Pad a hex value for use in transaction data
def pad(value, direction = 'right'):

    # Check if the value needs padding
    if(len(str(value)) % 64 == 0):

        # The value needs no padding
        return str(value)

    else:

        # Get the amount of padding required
        paddingRequired = 64 - (len(str(value)) % 64)

        # Check which direction to pad the value
        if(direction == 'left'):

            # Return the value padded left
            return str(value) + ('0' * paddingRequired)
        else:

            # Return the value padded right
            return ('0' * paddingRequired) + str(value)

# Function to convert from Wei to Ether
def weiToEther(wei):
    return wei / 1000000000000000000.0

# Get an Ethereum account by it's id
def getAccountByIndex(index):

    # Get the accounts from the geth instance
    allAccounts = accounts()

    # Return false if there is no account at the index
    if len(allAccounts) <= index or index < 0:
        return False

    # Return the account at the index
    return allAccounts[index]

# Get an Ethereum account by it's address
def getAccountByAddress(address):

    # Get the accounts from the geth instance
    allAccounts = accounts()

    # Loop through each account
    for index in xrange(len(allAccounts)):

        # Return this account if the address matches
        if allAccounts[index] == address or allAccounts[index] == '0x' + address:
            return allAccounts[index]

    # Loop completed, no account found with given name
    return False

# Convert a integer hex output from a ballot into a number
def responseToInteger(response):
    return hexToNumber(response)

# Convert a string hex output from a ballot into text
def responseToString(response):
    return hexToString(response[130:])

#TODO Convert a boolean hex output from a ballot into a boolean value

# Convert a candidates hex output from a ballot into an array
def responseToCandidates(response):
    return responseToString(response).split(',')

# Convert the voters hex output from a ballot into an array of addresses
def responseToVoters(response):

    # Get the voter addresses
    votersArrayString = response[130:]

    # Split the string into individual addresses
    return [str(votersArrayString[index+24:index+64]) for index in range(0, len(votersArrayString), 64)]

# Convert a public key hex output from a ballot into a number
def responseToPublicKey(response):
    return hexToNumber(response[130:])

# Convert the votes hex into an array of the votes
def responseToVoteValues(response):

    # Get the vote values
    votesArrayString = response[130:]

    # Split the string into individual values
    return [str(votesArrayString[index:index+64]) for index in range(0, len(votesArrayString), 64)]
