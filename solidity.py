# Import required modules
from solc import compile_files

# Function to compile a solidity contract in a given file
def compile(path):
    return compile_files([path]);
