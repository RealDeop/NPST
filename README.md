A Note From The Developer: i Will be Taking a break untill December third and in dec.3 update alpha 1.6 will be realeased 
Before Using Npst/nspt 
Please Read LICENSE and the mit license Here is a shortend Down version of it i repeat PLEASE READ THE LICENSE FILE AND THE  MIT LICENSE:
MIT License 

Copyright (c) 2023 RealDeop

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

1. Attribution Requirement: If you use, modify, or distribute the Software, you must include an attribution to the original author (RealDeop).

2. Offer Original Version: If you distribute a modified version of the Software, you must also make the original version of the Software available to recipients.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

NPST
NSPT (Numeral Script Processing Tool)
the code is a Python script designed to process a script stored in a file named "script.txt". The script allows for the numerical replacement of specific numbers within the script and supports a repetition feature for certain lines indicated by a special syntax.

Script Representation: The script is represented as text within "script.txt". Each line in this script is processed individually.

Numerical Replacement: The script is scanned for the command '/int (any number)', and each occurrence is replaced with an incremented number starting from 1.

Single Line Repetition Feature: every line in the script can be repeated a certain number of times. This is achieved by using the # symbol followed by a number indicating how many times the preceding line should be repeated.

Muilt Line Repetition Feature: Lines in the script can be repeated a certain number of times. This is achieved by using the /repeat -s to state the cloing lines followed by in the end of the reptiton lines /repeat followed by a number indicating how many times the preceding lines should be repeated.

 Processing Logic:
 The code reads the script from "script.txt".
 It processes the script line by line, replacing '/int (any number)' with an incremented starting from 1 and handling repetition as specified by the # symbol. and/or /repeat
 The modified script is saved to a file named "result.txt".

 User Interaction:
        The code provides a simple interaction where the user can request help by typing !help.
        When help is requested, instructions on how to use the script processing tool are displayed.
   

Commands:

    # / #end
   adds one to the specfied integer. example: [
   
    hi user/int 1 #end hi user/int 1
   ] 
    
    #start / #set
   sets the specfied integer to what you specify after. example: [
    
    #start 5 hi user/int 1 #start 10 hi user/int 1 
   ]
    
    #stop
   stops the script and saves what it changed. example use: [
   
    hi user/int 1 #end hi user/int 1 #start 4 hi user/int 1 #stop hi user 5 hi user 6 
   ]
    
    #rest
   sets the specfied integer to 1. example use: [ 
    
    hi/int 1 user/int 1 #end hi/int 1 user/int 1 #end #rest hi agian user/int 1 #end hi agian user /int 1 
    ].

    #var  
   makes a variable named to the named the user chooses 
   [
  
    #var by-RealDeop
   ]
  
in line commands:

    /int
   Main Use Set the specfied value to a integer
    
    /str
   Main Use Set the specfied value to a letter  

    /rdi
   Main Use generate a random integer using /rdi

    /rds
   Main Use generate a random string using /rds
   For more info check the commands.html page

  
    /var      
   it calls The variable assigend using #var or modifes its values 
 Result Output:
        Finally, it saves the modified script to "result.txt".

     /repeat and /repeat  -s 
   repeat a big  ol`chunk most of the time more then one line 
     
     /repeat -s 
   just specfies the place where /repeat may start repeating 

    /check
   Get A Checksum out of letters (letter meanany anything like symbols and numbers and letters)
needed lib:

        pip install subprocess
        
  if you wish to use the gui version download:
     
        pip install tkinter
        
