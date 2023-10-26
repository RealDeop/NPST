NPST
NSPT (Numeral Script Processing Tool)
The code is a Python script designed to process a script stored in a file named "script.txt". The script allows for the numerical replacement of specific numbers within the script and supports a repetition feature for certain lines indicated by a special syntax.

    Script Representation: The script is represented as text within "script.txt". Each line in this script is processed individually.

    Numerical Replacement: The script is scanned for the numeral '1', and each occurrence is replaced with an incremented number starting from 1.

    Repetition Feature: Lines in the script can be repeated a certain number of times. This is achieved by using the # symbol followed by a number indicating how many times the preceding line should be repeated.

    Processing Logic:
        The code reads the script from "script.txt".
        It processes the script line by line, replacing '1' with an incremented number and handling repetition as specified by the # symbol.
        The modified script is saved to a file named "result.txt".

    User Interaction:
        The code provides a simple interaction where the user can request help by typing !help.
        When help is requested, instructions on how to use the script processing tool are displayed.
    



    Hasum Function:
        The hasum function processes the script to handle the repetition feature specified by #.
        It repeats the lines preceding # as many times as indicated by the number following #.

    Commands:
    #/#end adds one to the start number. example: [ hi user1 #end hi user1] 
    #start sets the change number to what you specify after. example: [ #start 5 hi user1 #start 10 hi user1 ]
    #stop stops the script and saves what it changed. example use: [ hi user1 #end hi user1 #start 4 hi user1 #stop hi user 5 hi user 6 ]
    #rest resets the change number to 1. example use: [ hi1 user1 #end hi1 user1 #end #rest hi agian user1 #end hi agian user 1 ].

    Result Output:
        Finally, it saves the modified script to "result.txt".
