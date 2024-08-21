
# TODO: add rotors VI, VII, VIII since they have two notches
# TODO: add rotation of rotors (notch)

class Rotor:
    """
    Rotor object of an Enigma System. Takes a letter and returns a different letter corresponding to the rotation of the rotor.

    To be used as part of an Enigma System.
    """

    def __init__(self, ID, rotor, notch, start, position):
        """
        Parameters
        __________
        ID : identifcation name (char) of the rotor

        rotor : string indicating the rotation of the rotor

        notch : char indicating at which point of the rotor causes the rotor to its left to rotate

        start : starting rotation of the rotor

        position : location of rotor from left to right (IE furthest left rotor is 1, if all 5 rotors present, furthest right rotor is 5). 
        Used so that the furthest right rotor is rotated first before anything left until the notch is hit.

        Init function of the Rotor object.
        """
        self.map = {}
        input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for x in range(26):
            self.map[input[x]] = rotor[x]

        self.ID = ID
        self.rotor = rotor
        self.notch = notch
        self.rotation = start
        self.position = position

    def forward(self, letter):
        """
        Parameters
        __________
        letter : input letter (char)

        Takes input of a letter to return the index in the alphabet that that letter corresponds to.
        """
        if (letter == " "):
            return " "
        output = self.map[letter]
        return output
    
    def __str__(self):
        """
        Returns the ID of the rotor as a string 
        """
        return self.ID

