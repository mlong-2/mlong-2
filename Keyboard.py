alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

"""
Static class that acts as the keyboard of an Enigma system.
To be used as part of Enigma System.
"""

def forward(letter):
    """
    Parameters
    __________
    letter : input letter (char)

    Takes input of a letter to return the index in the alphabet that that letter corresponds to.
    """
    index = alphabet.find(letter)
    return index


def backward(index):
    """
    Parameters
    __________
    index : index in the alphabet

    Takes input of a index to return the letter in the alphabet that that index corresponds to.
    """
    letter = alphabet[index]
    return letter

