
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
        self.input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.output = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            A = pair[0]
            B = pair[1]
            pos_A = self.input.find(A)
            pos_B = self.output.find(B)
            self.input = self.input[:pos_A] + A + self.input[pos_A + 1:]
            self.input = self.input[:pos_B] + B + self.input[pos_B + 1:]

    def forward(self, index):
        """
        Parameters
        __________
        letter : input letter (char)

        Takes input of a letter to return the index in the alphabet that that letter corresponds to.
        """
        letter = self.output[index]
        index = self.input.find(letter)
        return index

    def backward(self, index):
        """
        Parameters
        __________
        index : index in the alphabet

        Takes input of a index to return the letter in the alphabet that that index corresponds to.
        """
        letter = self.input[index]
        index = self.output.find(letter)
        return index

