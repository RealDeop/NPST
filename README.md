NPST
NSPT (Numeral Script Processing Tool)
The code is a Python script designed to process a script stored in a file named "script.txt". or in a Gui menu based on your branch choice The script allows for the numerical replacement of specific numbers within the script and supports a repetition feature for certain lines indicated by a special syntax. using the commands bellow you can shape your 
script as you want it to be.
#/#end adds one to the start number. example:
[
hi user1
#end 
hi user1
#
]
#start sets the change number to what you specify after. example:
[
#start 5
hi user1
#start 10 
hi user1
]
#stop stops the script and saves what it changed. example use:
[
hi user1
#end
hi user1
#start 4 
hi user1
#stop
hi user 5
hi user 6
]
#rest resets the change number to 1. example use:
[
hi1 user1 
#end
hi1 user1 
#end
#rest
hi agian user1
#end
hi agian user 1
].
