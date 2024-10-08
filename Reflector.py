class Reflector:
    """
    Reflector object that takes a index and returns a different index.
    To be used as part of an Enigma System.
    """

    def __init__(self, ID, rotor):
        """
        Parameters
        __________
        ID : identification/name of the reflector object
        
        rotor : string indicating the rotation of the rotor

        Init function for the reflector obj.
        """
        self.ID = ID
        self.input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.output = rotor

    def reflect(self, letter):
        """
        Parameters
        __________
        index : index in the alphabet

        Takes input of a index to return the a different index corresponding to that index in the specificed rotor.
        """
        if (letter == " "):
            return " "
        x = self.input.find(letter)
        output = self.output[x]
        return output
    
    def __str__(self):
        """
        Returns the ID of the rotor as a string 
        """
        return self.ID

