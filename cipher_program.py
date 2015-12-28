"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message1.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Return the encryption using the deck from a placeholder
    file called DECK_FILENAME
    and the messages from a placeholder files MSG_FILENAME.
    If the MODE is 'e', encrypt
    although if the MODE is 'd' decrypt.
    REQ: A valid deck is a maximum of 26 cards and 2 Jokers.
    """
    # Opens the Deck that will be used to ecnrypt or decrypt a messsage
    deck_filehandle = open(DECK_FILENAME, 'r')
    # A list of int wil be returned after reading the deck that
    # will be used for encryption
    deck_list = cipher_functions.read_deck(deck_filehandle)
    # Opens the Message that will be either encrypted or decrypted
    my_file = open(MSG_FILENAME, "r")
    # Read the messages of the file
    my_read_file = cipher_functions.read_messages(my_file)
    # If the MODE choice was 'e' then encryption will occur
    # otherwise if MODE was 'd' then vice versa
    result = cipher_functions.process_messages(deck_list,
                                               my_read_file, MODE)
    deck_filehandle.close()
    my_file.close()
    for message in range(len(result)):
        print(result[message])

main()
