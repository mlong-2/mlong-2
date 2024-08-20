
# TODO: add rotors VI, VII, VIII since they have two notches
# TODO: add rotation of rotors (notch)

class Rotor:
    """
    Rotor object of an Enigma System. Takes a letter and returns a different letter corresponding to the rotation of the rotor.

    To be used as part of an Enigma System.
    """

    def __init__(self, ID, rotor, notch):
        """
        Parameters
        __________
        ID : identifcation name (char) of the rotor

        rotor : string indicating the rotation of the rotor

        notch : char indicating at which point of the rotor causes the rotor to its left to rotate

        Init function of the Rotor object.
        """
        self.input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.ID = ID
        self.output = rotor
        self.notch = notch

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
    
    def __str__(self):
        """
        Returns the ID of the rotor as a string 
        """
        return self.ID

