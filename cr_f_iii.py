#!/usr/bin/python3

#RSA Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import sys

# IMPORTANT: The block size MUST be less than or equal to the key size!
# (Note: The block size is in bytes, the key size is in bits. There
# are 8 bits in 1 byte.)
DEFAULT_BLOCK_SIZE = 128 # 128 bytes
BYTE_SIZE = 256 # One byte has 256 different values.

def main_d():
    # Runs a test that encrypts a message to a file or decrypts a message
    # from a file.
    filename = cr_k_i.txt # the file to write to/read from

    mode = 'decrypt' # set to 'decrypt'

    if mode == 'decrypt':
        privKeyFilename = cr_k_iii.txt
        #print('Reading from %s and decrypting...' % (filename))
        decryptedText = readFromFileAndDecrypt(filename, privKeyFilename)

        txt = decryptedText
        fo = open(filename, 'w')
        fo.write(txt)
        fo.close()

    else:
        pass

def getTextFromBlocks(blockInts, messageLength, blockSize=DEFAULT_BLOCK_SIZE):
    # Converts a list of block integers to the original message string.
    # The original message length is needed to properly convert the last
    # block integer.
    message = []
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i < messageLength:
                # Decode the message string for the 128 (or whatever
                # blockSize is set to) characters from this block integer.
                asciiNumber = blockInt // (BYTE_SIZE ** i)
                blockInt = blockInt % (BYTE_SIZE ** i)
                blockMessage.insert(0, chr(asciiNumber))
        message.extend(blockMessage)
    return ''.join(message)

def decryptMessage(encryptedBlocks, messageLength, key, blockSize=DEFAULT_BLOCK_SIZE):
    # Decrypts a list of encrypted block ints into the original message
    # string. The original message length is required to properly decrypt
    # the last block. Be sure to pass the PRIVATE key to decrypt.
    decryptedBlocks = []
    n, d = key
    for block in encryptedBlocks:
        # plaintext = ciphertext ^ d mod n
        decryptedBlocks.append(pow(block, d, n))
    return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)


def readKeyFile(keyFilename):
    # Given the filename of a file that contains a public or private key,
    # return the key as a (n,e) or (n,d) tuple value.
    fo = open(keyFilename)
    content = fo.read()
    fo.close()
    keySize, n, EorD = content.split(',')
    return (int(keySize), int(n), int(EorD))

def readFromFileAndDecrypt(messageFilename, keyFilename):
    # Using a key from a key file, read an encrypted message from a file
    # and then decrypt it. Returns the decrypted message string.
    keySize, n, d = readKeyFile(keyFilename)


    # Read in the message length and the encrypted message from the file.
    fo = open(messageFilename)
    #fo.write(decryptMessage)
    content = fo.read()
    messageLength, blockSize, encryptedMessage = content.split('_')
    messageLength = int(messageLength)
    blockSize = int(blockSize)

    # Check that key size is greater than block size.
    if keySize < blockSize * 8: # * 8 to convert bytes to bits
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size. Did you specify the correct key file and encrypted file?' % (blockSize * 8, keySize))

    # Convert the encrypted message into large int values.
    encryptedBlocks = []
    for block in encryptedMessage.split(','):
        encryptedBlocks.append(int(block))

    # Decrypt the large int values.
    return decryptMessage(encryptedBlocks, messageLength, (n, d), blockSize)


# If rsaCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main_d()

