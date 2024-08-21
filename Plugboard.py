
class Plugboard:
    """
    Plugboard of the enigma system. Works by swapping letters.
    Example: A becomes Z and Z becomes A.

    Input is provided as a two digit string or a list of 2 digit strings.
    Example: "AB" or ["AB", "CD", "ZP"]

    To be used as part of an Enigma System.
    """

    def __init__(self, pairs):
        """
        Parameters
        __________
        pairs : list of two char strings to be swapped

        Takes input list of two char strings that will be swapped. 
        """
        self.map = {}
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for x in range(26):
            self.map[alphabet[x]] = alphabet[x]
        
        for pair in pairs:
            char1 = pair[0]
            char2 = pair[1]
            self.map[char1] = char2
            self.map[char2] = char1

    def forward(self, letter):
        """
        Parameters
        __________
        index : input index of the alphabet

        """
        if (letter == " "):
            return " "
        return self.map[letter]
    
    def resetMap(self):
        self.map = {}
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for x in range(26):
            self.map[alphabet[x]] = alphabet[x]

