# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here: chr(ord('a')+0)


def clean_message(message):
    '''(str) -> str
    The parameter is a message (i.e. it is a str that contains only one
    line of text).

    Return a copy of the message that includes only its alphabetical
    characters, where each of those characters has been converted to uppercase.
    >>> clean_message("w.'a13.;'s;12345E;.f];639';5168.;'4;")
    'WASEF'
    >>> clean_message('=-!@#$%^%&$%&ZZXXCC     ')
    'ZZXXCC'
    >>> clean_message('            /A/       ')
    'A'
    >>> clean_message('Lake Hylia')
    LAKEHYLIA
    '''
    new_message = ''
    # Clean the message of spaces
    message = message.strip()
    # Make all the letters in message uppercase
    message = message.upper()
    # Loop through every charecter in the string messages
    for element in message:
        # If the charecter is alphanumeric then append it to new_message
        if (element.isalpha()):
            # Add the alphanumeric charecters to the string
            new_message += element
    return new_message


def encrypt_letter(char, keystream_value):
    '''(str, int) -> str
    The first parameter is a single character and the second represents a
    keystream value.
    Apply the keystream value to the character to encrypt the character,
    and return the result.
    >>> encrypt_letter('a',8)
    'I'
    >>> encrypt_letter('F',2)
    'H'
    >>> encrypt_letter('Z',25)
    'Y'
    >>> encrypt_letter('A',26)
    'A'
    >>> encrypt_letter('z',12)
    'L'
    >>> encrypt_letter('Z',12)
    'L'
    >>> encrypt_letter('G',0)
    'G'
    '''
    lower_case_char = char.lower()
    # This will make it so that a which has an ord(a) value of 97 will be zero
    char_value = ord(lower_case_char) - 97
    # Add the keystream value to encrpyt the charecter
    new_char_value = char_value + keystream_value
    # Our letters are only from 0 - 25
    while(new_char_value >= 26):
        new_char_value -= 26
    new_char = chr(ord('a') + new_char_value)
    # Make the charecters into uppercase format
    new_char = new_char.upper()
    return new_char


def decrypt_letter(uppercase_char, keystream_value):
    '''(str, int) -> str
    The first parameter is a single uppercase character and the second
    represents a keystream value.

    Apply the keystream value to the character to decrypt the character,
    and return the result.
    >>> decrypt_letter('x',12)
    'L'
    >>> decrypt_letter('X',12)
    'L'
    >>> decrypt_letter('Z',12)
    'N'
    >>> decrypt_letter('A',12)
    'O'
    >>> decrypt_letter('y',12)
    'M'
    >>> decrypt_letter('y',0)
    'Y'
    '''
    uppercase_char = uppercase_char.lower()
    # Using ASCii Table we can find the letter from the number
    uppercase_char_value = ord(uppercase_char) - 97
    new_uppercase_char_value = uppercase_char_value - keystream_value
    # If the number value for the letter is less than zero add 26
    while(new_uppercase_char_value < 0):
        new_uppercase_char_value += 26
    # Now we can find out what letter was chosen based on the number generated
    new_uppercase_char = chr(ord('a') + new_uppercase_char_value)
    # Make the charecters into uppercase format
    new_uppercase_char = new_uppercase_char.upper()
    return new_uppercase_char


def swap_cards(deck_list, index):  # Check for examples!!!!!!!
    '''(list of int, int) -> NoneType
    The first parameter represents a deck of cards and the second represents
    an index into the deck.

    Swap the card at the index with the card that follows it. Treat the deck
    as circular: if the card at the index is on the bottom of the deck,
    swap that card with the top card.

    (Note that in this and all functions that do something to the deck, the
    function doesn't return anything. The deck is to be mutated.)

    '''
    # If the Joker is at the end of the list place it in the front but
    # If the joker is not at the end just swap values with the number
    # infront of it

    # Incase the number of elements in the deck changes we can check if the
    # JOKER is at the end of the list so that we do not go out of range/index
    if(index == (len(deck_list) - 1)):
        # Take the position of the JOKER and switch it with the first card
        # if the card is at the end of the deck
        (deck_list[index], deck_list[0]) = (deck_list[0], deck_list[index])
    else:
        # Take the position of the JOKER and swap it
        # with the card in front of it
        (deck_list[index], deck_list[index+1]) = (deck_list[index+1],
                                                  deck_list[index])


def move_joker_1(deck_list):
    '''(list of int) -> NoneType
    The parameter represents a deck of cards.

    This is step 1 of the algorithm. Find JOKER1 and swap it with the card
    that follows it. Treat the deck as circular.
    0-27 is the list so if index_ofjoker == 27 switch with top
    >>>move_joker_1([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24,
    2, 27, 5, 8, 11, 14, 17, 20, 23, 26]

    >>> deck_list = [4, 3, 5, 9, 27, 8,9,13]
    >>> move_joker_1(deck_list)
    >>> deck_list
    [4, 3, 5, 9, 8, 27, 9, 13]
    >>> move_joker_1(deck_list)
    >>> deck_list
    [4, 3, 5, 9, 8, 9, 27, 13]
    >>> move_joker_1(deck_list)
    >>> deck_list
    [4, 3, 5, 9, 8, 9, 13, 27]
    >>> move_joker_1(deck_list)
    >>> deck_list
    [27, 3, 5, 9, 8, 13, 4]
    '''
    # Get the Index location of where the Joker1 is.
    index_of_joker1 = deck_list.index(JOKER1)
    # Swap the joker with the card that follows it. (Deck is mutated)
    swap_cards(deck_list, index_of_joker1)


def move_joker_2(deck_list):
    '''(list of int) -> NoneType
    The parameter represents a deck of cards.
    This is step 2 of the algorithm. Find JOKER2 and move it two cards down.
    Treat the deck as circular.
    >>> deck_list = [4, 3, 5, 9, 28, 8, 18, 13]
    >>> move_joker_2(deck_list)
    >>> deck_list
    [4, 3, 5, 9, 8, 18, 28, 13]
    >>> move_joker_2(deck_list)
    >>> deck_list
    [28, 3, 5, 9, 8, 18, 13, 4]
    >>> move_joker_2(deck_list)
    >>> deck_list
    [3, 5, 28, 9, 8, 18, 13, 4]
    '''
    # Get the Index location of where the Joker2 is.
    index_of_joker2 = deck_list.index(JOKER2)
    # Swap the joker with the card that follows it. (Deck is mutated)
    swap_cards(deck_list, index_of_joker2)
    index_of_joker2 = deck_list.index(JOKER2)
    # Swap the joker with the card that follows it. (Deck is mutated)
    swap_cards(deck_list, index_of_joker2)


def triple_cut(deck_list):  # Double check this  (ISSUES WITH CLEAR)
    '''(list of int) -> NoneType
    The parameter represents a deck of cards.
    REQ: The deck must only have one 27 and one 28
    This is step 3 of the algorithm. Find the two jokers and do a triple cut.
    >>> triple_cut([1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 28, 9, 12, 15,
    18, 21, 24, 2, 27, 5, 8, 11, 14, 17, 20, 23, 26])
    [5, 8, 11, 14, 17, 20, 23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1,
    4, 7, 10, 13, 16, 19, 22, 25, 3, 6]
    >>> deck_list = [4, 3, 5, 9, 28, 8, 27, 13]
    >>> triple_cut(deck_list)
    >>> deck_list
    [13, 28, 8, 27, 4, 3, 5, 9]
    >>> deck_list = [4, 3, 5, 9, 11, 8, 27, 28]
    >>> triple_cut(deck_list)
    >>> deck_list
    [27, 28, 4, 3, 5, 9, 11, 8]
    >>> deck_list = [28, 3, 5, 9, 14, 8, 12, 27]
    >>> triple_cut(deck_list)
    >>> deck_list
    [28, 3, 5, 9, 14, 8, 12, 27]
    >>> deck_list = [27, 3, 5, 9, 14, 8, 12, 28]
    >>> triple_cut(deck_list)
    >>> deck_list
    [27, 3, 5, 9, 14, 8, 12, 28]
    >>> deck_list = [16, 3, 5, 9, 14, 8, 28, 27]
    >>> triple_cut(deck_list)
    >>> deck_list
    [28, 27, 16, 3, 5, 9, 14, 8]
    '''
    # Find the index number of the joker1 and joker2
    index_of_joker1 = deck_list.index(JOKER1)
    index_of_joker2 = deck_list.index(JOKER2)
    # If joker1 is before of joker2 than triple cut using Joker1 as reference
    if (index_of_joker1 < index_of_joker2):
        # Get all the cards before the first joker excluding the first joker
        temp_list_left = deck_list[:index_of_joker1]
        # Get all the cards after the second joker excluding the second joker
        temp_list_right = deck_list[index_of_joker2+1:]
        # Get all the cards inbeteweem both jokers
        temp_list_middle = deck_list[index_of_joker1:index_of_joker2+1]
        # Add all the lists back in the appropriate order to complete
        # triple cut
        del deck_list[:]
        deck_list += temp_list_right + temp_list_middle + temp_list_left
    else:
        # Get all the cards before the first joker excluding the first joker
        temp_list_left = deck_list[:index_of_joker2]
        # Get all the cards after the second joker excluding the second joker
        temp_list_right = deck_list[index_of_joker1+1:]
        # Get all the cards inbeteweem both jokers
        temp_list_middle = deck_list[index_of_joker2:index_of_joker1+1]
        # Add all the lists back in the appropriate order to complete a
        # triple cut
        del deck_list[:]
        deck_list += temp_list_right + temp_list_middle + temp_list_left


def insert_top_to_bottom(deck_list):
    '''(list of int) -> NoneType

    REQ: The value of card in the deck cannot be greater than the value
    of len(deck_list) -1
    REQ : The Last Case Value cannot be equal to length of list

    Return a deck_list by getting the bottom card of the deck and moving
    that many cards from the top of the deck to the bottom inserting them
    just before the last card.
    Special case: if the bottom card is JOKER2, use JOKER1 as the number
    of cards.
    >>> insert_top_to_bottom([5, 8, 11, 14, 17, 20, 23, 26, 28, 9, 12, 15,
    18, 21, 24, 2, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6])
    [23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, 4, 7, 10, 13, 16,
    19, 22, 25, 3, 5, 8, 11, 14, 17, 20, 6]

    >>> deck_list = [4, 3, 5, 9, 28, 8, 27, 3]
    >>> insert_top_to_bottom(deck_list)
    >>> deck_list
    [9, 28, 8, 27, 4, 3, 5, 3]

    >>> deck_list = [4, 3, 5, 9, 11, 28, 27, 1]
    >>> insert_top_to_bottom(deck_list)
    >>> deck_list
    [3, 5, 9, 11, 28, 27, 4, 1]

    >>> deck_list = [28, 27, 5, 9, 14, 8, 12, 5]
    >>> insert_top_to_bottom(deck_list)
    >>> deck_list
    [8, 12, 28, 27, 5, 9, 14, 5]

    >>> deck_list = [27, 3, 5, 9, 28, 8, 12, 7]
    >>> insert_top_to_bottom(deck_list)
    >>> deck_list
    [27, 3, 5, 9, 28, 8, 12, 7]

    >>> deck_list = [16, 27, 5, 9, 14, 3, 28, 8]
    >>> insert_top_to_bottom(deck_list)
    >>> deck_list
    [16, 27, 5, 9, 14, 3, 28, 8]
    '''
    # Find the value of the of the last card in the deck (bottom card)
    number_of_cards = deck_list[len(deck_list)-1]
    # If the value of the card is JOKER2 then use JOKER1 as the value
    if (number_of_cards == JOKER2):
        # Set the number of cards as the value of JOKER1
        number_of_cards = JOKER1
    # Gather the first number_of_cards from the start
    temp_list_start = deck_list[:number_of_cards]
    # Gather the last element of the list in list format
    if (number_of_cards == len(deck_list)):
        temp_list_end = []
    else:
        temp_list_end = deck_list[(len(deck_list)-1):(len(deck_list))]
    # Gather the middle of the deck
    temp_list_middle = deck_list[number_of_cards:len(deck_list)-1]
    # Stitch the whole deck together
    del deck_list[:]
    deck_list += temp_list_middle + temp_list_start + temp_list_end


def get_card_at_top_index(deck_list):
    '''(list of int) -> int
    The parameter represents a deck of cards.

    Look at the top card. Using that value
    as an index, return the card in that deck at that index. Special case:
    if the top card is JOKER2, use JOKER1 as the index.
    >>> get_card_at_top_index([23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27,
    1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 5, 8, 11, 14, 17, 20, 6])
    11

    >>> deck_list = [4, 3, 5, 9, 28, 8, 27, 3]
    >>> get_card_at_top_index(deck_list)
    >>> deck_list
    [9, 28, 8, 27, 4, 3, 5, 3]
    8
    >>> deck_list = [4, 3, 5, 9, 11, 28, 27, 1]
    >>> get_card_at_top_index(deck_list)
    >>> deck_list
    [3, 5, 9, 11, 28, 27, 4, 1]
    11
    >>> deck_list = [28, 2, 5, 9, 14, 8, 12, 27]
    >>> get_card_at_top_index(deck_list)
    >>> deck_list


    >>> deck_list = [27, 3, 5, 9, 2, 8, 12, 28]
    >>> get_card_at_top_index(deck_list)
    >>> deck_list
    [27, 3, 5, 9, 28, 8, 12, 7]

    >>> deck_list = [16, 27, 5, 9, 14, 3, 28, 8]
    >>> get_card_at_top_index(deck_list)
    >>> deck_list
    '''
    # Get the value of the top card
    index_by_value = deck_list[0]
    # If the card value is JOKER2 use JOKER1
    if (index_by_value == JOKER2):
        index_by_value = JOKER1
    # Get the Keystream from the value of the int and the index
    # -> (index_by_value)
    value_at_index = deck_list[index_by_value]
    # Making sure the value of the int is not a joker value
    if((value_at_index == JOKER1) or (value_at_index == JOKER2)):
        value_at_index = get_next_keystream_value(deck_list)
    # Set the new keystream value to the improved one
    key_stream_value = value_at_index
    return key_stream_value


def get_next_value(deck_list):
    '''(list of int) -> int
    Return the next potential keystream after it has been encrypted
    with all five steps of the algorithm.
    >>> get_next_value([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6,
    9, 12, 15, 18, 21,
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    11
    >>> deck_list = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6,
    9, 12, 15, 18, 21,
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_next_value(deck_list)
    >>> get_next_value(deck_list)
    9
    '''
    # Runs the 5 Step Algorithem
    move_joker_1(deck_list)
    move_joker_2(deck_list)
    triple_cut(deck_list)
    insert_top_to_bottom(deck_list)
    # This function return an int value
    value_of_keystream = get_card_at_top_index(deck_list)
    return value_of_keystream


def get_next_keystream_value(deck_list):
    '''(list of int) -> int
    The parameter represents a deck of cards.

    This is the function that repeats all five steps of the algorithm
    (call get_next_value to get potential keystream values!) until a
    valid keystream value (a number in the range 1-26) is produced.

    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_next_keystream_value(deck)
    11
    >>> get_next_keystream_value(deck)
    9
    '''
    value_at_index = get_next_value(deck_list)
    # Loops untill the value_at_index is a number inbetween 1 - 26
    while ((value_at_index == JOKER1) or (value_at_index == JOKER2) or
           not((value_at_index >= 1) and (value_at_index <= 26))):
        # Calls the algorithem to get the next value
        value_at_index = get_next_value(deck_list)
    return value_at_index


def process_message(deck_list, message, choice):
    '''(list of int, str, str) -> str
    The first parameter represents a deck of cards. The second represents a
    message to encrypt or decrypt based on the third parameter, which is
    either 'e' (to encrypt) or 'd' (to decrypt).

    Return the encrypted or decrypted message. Note that the message
    might contain non-letters.
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,
    18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> message = 'EQFZSRTEAPNXLSRJAMNGAT'
    >>> mode = 'd'
    >>> process_message(deck, message, mode)
    'thisisitthemastersword'
    '''
    # This will hold the new encrypted or decrypted message
    result = ''
    if (choice == "e"):
        # Cleans the message to remove the non-letters
        message = clean_message(message)
        for char in message:
            # Generating a new KeyStream value per charecter
            keystream_value = get_next_value(deck_list)
            # Add the new encrypted letter to the final result
            result += encrypt_letter(char, keystream_value)
    else:
        # Cleans the message to remove the non-letters
        message = clean_message(message)
        for char in message:
            # Generating a new KeyStream value per charecter
            keystream_value = get_next_value(deck_list)
            # Add the new encrypted letter to the final result
            result += decrypt_letter(char, keystream_value)
    return result


def process_messages(deck_list, message_list, choice):  # Check
    '''(list of int, list of str, str) -> list of str
    The first parameter represents a deck of cards. The second represents a
    list of messages to encrypt or decrypt based on the third parameter,
    which is either 'e' (to encrypt) or 'd' (to decrypt).

    Return the list of encrypted or decrypted messages.
    REQ: The mode's values are "e" or "d"
    REQ: The deck must have a maximum of 28 cards and 2 Jokers
    >>> process_messages([1,2,3,4,5,6,7],['LOL','LMFAO','GreatTheJob'],'e')
    ['NTN', 'ONHCS', 'KUFDVYIHMQF']
    >>> process_messages([1,2,3,4,5,6,7],['NTN', 'ONHCS', 'KUFDVYIHMQF'],'d')
    ['LOL','LMFAO','GreatTheJob']
    '''
    result = ''
    counter = 0
    new_message_list = []
    length = 0
    new_message_list_life = []
    if (choice == "e"):
        for message in message_list:
            encryption = ''
            # Loop through each charecter in the string
            for char in message:
                # Get the keystream value
                keystream_value = get_next_value(deck_list)
                # Get the encrypted charecter with the keystream value
                result = encrypt_letter(char, keystream_value)
                # Add the new encrypted charecter to a string
                encryption += result
            # Add the string to one element of the list
            new_message_list.append(encryption)
    else:
        for message in message_list:
            decryption = ''
            for char in message:
                keystream_value = get_next_value(deck_list)
                result = decrypt_letter(char, keystream_value)
                decryption += result
            new_message_list.append(decryption)
    return new_message_list


def read_messages(file_handle):
    '''(io.TextIOWrapper) -> list of str
    The parameter represents an open message file, which contains one message
    per line.
    Read and return the contents of the file as a list of messages. Strip
    the newline from each line.
    Note: you don't have to provide example calls for
    functions that read files.
    >>> if (__name__ == '__main__'):
    >>> my_file = open("message1.txt", "r")
    >>> print(read_messages(my_file))
    >>> my_file.close()
    ['This is it! The master sword!', "No, this can't be it. Too bad."]
    '''
    # An empty list that contains all the words in the file
    deck_list = []
    # Loops through the file until it has reached the end of the file
    with file_handle as function:
        # Loops through each line of the file
        for line_read in function:
            line_read = line_read.strip()
            # Add each word as a string to a list
            deck_list.append(line_read)
    return deck_list


def read_deck(file_handle):  # Do not open files
    '''(io.TextIOWrapper) -> list of int
    Reutrn the contents of the file as a list of integers.
    REQ: No strings in the file
    >>> if (__name__ == '__main__'):
    >>> my_file = open("deck1.txt", "r")
    >>> print(read_deck(my_file))
    >>> my_file.close()
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21,
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> if (__name__ == '__main__'):
    >>> my_file = open("deck2.txt", "r")
    >>> print(read_deck(my_file))
    >>> my_file.close()
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21,
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    '''
    # An empty list that contains all the integers in the file
    deck_list = []
    # Loops through the file until it has reached the end of the file
    with file_handle as function:
        # Loops through each line of the file
        for line_read in function:
            # Add each number as a int to a list
            deck_list += [int(number) for number in line_read.split()]
    return deck_list

