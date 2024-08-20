MAIN:
import Enigma


Enigma.main()




ENIGMA:
from Rotor import Rotor
from Reflector import Reflector
import Keyboard
from Plugboard import Plugboard
import PySimpleGUI as display

# TODO : plugboard doesn't seem to work
# TODO : need to set initial rotation of rotors and actually do rotation

# rotor and notch information found on https://en.wikipedia.org/wiki/Enigma_rotor_details
I = Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("II", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("III", "BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("IV", "ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("V", "VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

A = Reflector("A", "EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("B", "YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("C", "FVPJIAOYEDRZXWGCTKUQSBNMHL")


def processSignal(original, rotors, plugs, reflector):
    """
    parameters
    __________
    original : input message string

    rotors : list of up to 5 rotors in order of placement

    plugs : Plugboard object indicating which letters are swapped

    reflector : Reflector object indicating which reflector is present
    """
    output = ""
    for letter in original:
        if letter == " ":
            output += " "
        else:
            x = Keyboard.forward(letter)
            x = plugs.forward(x)
            for rotor in rotors:
                x = rotor.forward(x)
            x = reflector.reflect(x)
            for rotor in reversed(rotors):
                x = rotor.backward(x)
            x = plugs.backward(x)
            x = Keyboard.backward(x)
            output += x
    return output


def main():
    """
    main function for the Enigma System that starts the entire process.
    """

    currentRotors = []
    currentReflector = A
    currentPlugs = []
    plugSelection = []

    alphabetList = [*"ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    settings_layout = [
        [
            display.Text("Select your Rotors from left to right: ")
        ],
        [   
            # max is 5 rotors
            display.Combo([I, II, III, IV, V], readonly=True, key="rotor1"), 
            display.Combo([I, II, III, IV, V], readonly=True, key="rotor2"),
            display.Combo([I, II, III, IV, V], readonly=True, key="rotor3"),
            display.Combo([I, II, III, IV, V], readonly=True, key="rotor4"),
            display.Combo([I, II, III, IV, V], readonly=True, key="rotor5")
        ],
        [
            display.Text("Select your starting rotations of the Rotors: ")
        ],
        [
            display.Combo([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26], readonly=True, key="rotor1Rotation", size=(4,1), default_value=1),
            display.Combo([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26], readonly=True, key="rotor2Rotation", size=(4,1), default_value=1),
            display.Combo([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26], readonly=True, key="rotor3Rotation", size=(4,1), default_value=1),
            display.Combo([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26], readonly=True, key="rotor4Rotation", size=(4,1), default_value=1),
            display.Combo([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26], readonly=True, key="rotor5Rotation", size=(4,1), default_value=1)
        ],
        [
            display.Text("Select your Reflectors: "),
            display.Combo([A, B, C], readonly=True, key="reflector", default_value=A, size=(4,1))
        ],
        [
            display.Text("Select the first letter you would like to plug on the plugboard:      "),
            display.Combo(alphabetList, readonly=True, key="plug1Char", size=(4,1))
        ],
        [
            display.Text("Select the second letter you would like to plug on the plugboard: "),
            display.Combo(alphabetList, readonly=True, key="plug2Char", size=(4,1))
        ],
        [
            display.Button("Add plug combination", key="AddPlugs"),
            display.Button("Reset Plugs", key="ResetPlugs")
        ],
        [
            display.Text("Current Selected plugs: ", key="currPlugs")
        ],
        [
            display.Button("Save")
        ]
    ]
    keyboard_layout = [
        [
            display.Text("Processed Message: ")
        ],
        [
            display.Text(size=(50, 1), key="OutputMSG")
        ],
        [
            display.Text("Enter your Message: ")
        ], 
        [
            display.In(size=(50, 1), enable_events=True, key="InputMSG")
        ]
    ]

    layout = [[display.TabGroup([[display.Tab("Keyboard", keyboard_layout), display.Tab("Settings", settings_layout)]])]]
    window = display.Window("Enigma", layout)

    while True:
        event, values = window.read()
        
        if event == "InputMSG":
            # output = processSignal(values['InputMSG'].upper(), [I, II, III], Plugboard(["AB", "XZ"]), A)
            output = processSignal(values['InputMSG'].upper(), currentRotors, Plugboard(currentPlugs), currentReflector)
            window["OutputMSG"].update(value=output)
        
        elif event == "Save":
            # resetting values
            currentRotors = []
            currentReflector = ""
            currentPlugs = []
    
            if values["rotor1"] != "":
                currentRotors.append(values["rotor1"])
            if values["rotor2"] != "" and values["rotor2"] not in currentRotors:
                    currentRotors.append(values["rotor2"])
            if values["rotor3"] != "" and values["rotor3"] not in currentRotors:
                currentRotors.append(values["rotor3"])
            if values["rotor4"] != "" and values["rotor4"] not in currentRotors:
                currentRotors.append(values["rotor4"])
            if values["rotor5"] != "" and values["rotor5"] not in currentRotors:
                currentRotors.append(values["rotor5"])
            currentReflector = values["reflector"]
            currentPlugs = plugSelection

        elif event == "AddPlugs":
            if values["plug1Char"] != values["plug2Char"]:
                plugSelection.append(' '.join(values["plug1Char"]) + ' '.join(values["plug2Char"]))
                window["currPlugs"].update(value=plugSelection)
                
                alphabetList.remove(values["plug1Char"])
                alphabetList.remove(values["plug2Char"])

                window["plug1Char"].update(values=alphabetList)
                window["plug2Char"].update(values=alphabetList)
        
        elif event == "ResetPlugs":
            plugSelection = []
            alphabetList = [*"ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
            window["plug1Char"].update(values=alphabetList)
            window["plug2Char"].update(values=alphabetList)
            window["currPlugs"].update(value=plugSelection)

        elif event == display.WIN_CLOSED:
            break















KEYBOARD:
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









Plugboard:

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




REFLECTOR:
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

    def reflect(self, index):
        """
        Parameters
        __________
        index : index in the alphabet

        Takes input of a index to return the a different index corresponding to that index in the specificed rotor.
        """
        letter = self.output[index]
        index = self.input.find(letter)
        return index
    
    def __str__(self):
        """
        Returns the ID of the rotor as a string 
        """
        return self.ID



ROTOR:

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





