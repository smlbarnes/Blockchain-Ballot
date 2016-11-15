# Import required modules
import os

# Write to the file system
def save(filePath, content):

    # Open a file at the given path
    file = open(filePath, 'w')

    # Write the content to the file
    file.write(content)

    # Close the file
    file.close()

# Read and return a file's contents
def read(filePath):
    return open(filePath, 'r').read()

# Delete a file from the file system
def delete(filePath):
    os.remove(filePath)

# Convert an array to a csv
def arrayToCsv(array):

    # Initalise the csv
    csv=""

    # Loop through the array
    for index in range(len(array)):

        # Only add a trailing comma if this isn't the first value
        if index > 0: csv += ','

        # Append the array element to the csv
        csv += str(array[index])

    # Return the completed csv
    return csv
