import os

# Declare global variables
file_found = False
current_directory = os.path.dirname(os.path.abspath(__file__))
directory = os.path.dirname(os.path.abspath(__file__))
prevuse = False
rwscrptf = False

def values():
    global prevuse, rwscrptf  # Declare global variables
    help_input = input("If you want help, type !help or !commands. If not, press Enter.\n")
    if help_input == "!help":
        print("To use nspt.py, create a script.txt file and type anything you want. Replace the number you want to change numerically with 1. To make the script change the number, put a # when you want to change the number and add one to it. For example: line1 and word 1 # line1 and word 1 \n")
    elif help_input == "!commands":
        print("Here are all the commands and how to use them.\n #10 (or any number you want can be used to copy the line before the # and repeat using the number you put) \n #start (is used to change the start number to anything you want).\n #set (sets the starting number to a specific value).\n #stop (stops the code and saves the changes) \n #end (is the same as #, meaning it adds to the starting number by 1). \n #rest (resets the starting number to 1) ")
    
    # Define the filename you want to search for
    filename = 'script.txt'

    # Construct the full path to the file in the current directory
    file_path = os.path.join(current_directory, filename)

    # Check if the file exists
    if os.path.exists(file_path):
        print("Program Started.")
def filenotfound404():
    global prevuse, rwscrptf  # Declare global variables
    if file_found == True and prevuse == False:
        err_f_404 = input("Error: script.txt not found. Please enter the directory or enter the script\n")
    if file_found == True and prevuse == True:
        err_f_404 = input("Whoa! It looks like you didn't type in the script. But thankfully, you can enter the directory or enter the script\n")
    filename = 'script.txt'

    # Construct the full path to the file
    file_path = os.path.join(directory, filename)
    
    # Check if the file exists
    if os.path.exists(file_path):
        print("File found. Program Started")
    else:
        contdir = input("Please confirm that you typed in your script.txt file but not your file directory. If not, type 'n'. If yes, type 'y' \n")  # contdir means confirm not a dir
        if contdir.lower() == "y":
            rwscrptf = True  # The user is now using raw script file mode, which means they typed in the script contents 
        else:
            prevuse = True  # Inform the file not found 404 function that the user used it previously wrong and is now in need to correct it to use nspt 
            filenotfound404()  # Recall the file not found 404 function

def hasum(script):
    lines = script.splitlines()
    result = ""

    for line in lines:
        if line.startswith("#") or line.strip() == "#end" or line.strip() == "#rest" or line.strip() == "#stop":
            try:
                amount = int(line[1:])
                for i in range(amount):
                    result += lines[lines.index(line) - 1] + "\n"
            except ValueError:
                result += line + "\n"
        else:
            result += line + "\n"

    return result

def replace_numbers(script):
    start_number = 1
    result = ""
    stop_reached = False

    for line in script.splitlines():
        if line.strip() == "#" or line.strip() == "#end":
            start_number += 1
            if line.strip() == "#end":
                start_number -= 1  # Adjust to increment by 1 for #end
        elif line.strip() == "#rest":
            start_number = 1
        elif line.strip() == "#stop":
            stop_reached = True
            break
        elif line.startswith("#start"):
            try:
                start_number = int(line.split()[1])
            except ValueError:
                print("Invalid #start command. Using default start number (1).")
            except IndexError:
                print("Invalid #start command. Not adding an index will result in an error. Please change the script.")
        elif line.startswith("#set"):
            try:
                start_number = int(line.split()[1])
            except ValueError:
                print("Invalid #set command. Value must be an integer.")
            except IndexError:
                print("Invalid #set command. Please provide an integer value.")
        else:
            while "/int" in line:
                int_index = line.find("/int")
                if int_index != -1:
                    try:
                        # Extract the number following "/int"
                        number = int(line[int_index + 4:].split()[0])
                        if number == 1:
                            line = line.replace("/int 1", str(start_number))
                        else:
                            line = line.replace("/int " + str(number), str(start_number))
                    except ValueError:
                        print("Invalid /int format. Using default value 1.")
            
            # Handle /str command
            letters = 'abcdefghijklmnopqrstuvwxyz'

            if start_number < 26:
                specified_order = start_number
            if start_number > 25:
                times_over_25 = math.ceil(start_number / 26)  # Calculate how many times it's over 26
                specified_order = start_number - 26 * (times_over_25 - 1)
            while "/str" in line:
                str_index = line.find("/str")
                strr = str(line[str_index + 4:].split()[0])
                for letter in letters:
                    if letter.lower() == strr:
                        strr = letter.lower()
                        upper = False
                    elif letter.upper() == strr:
                        strr = letter.upper()
                        upper = True
                    line = line.replace("/str " + str(strr), str(letters[(specified_order - 1)]))
                

            result += line + "\n"
            start_number += 1

    return result, stop_reached

if __name__ == "__main__":

    values()  # Call the help function
    if rwscrptf == False:
        with open("script.txt", "r") as file:
            script = file.read()
    if rwscrptf == True:
        script = err_f_404
    script_with_hasum = hasum(script)
    replaced_script, stop_reached = replace_numbers(script_with_hasum)

    with open("result.txt", "w") as file:
        file.write(replaced_script)

    print("Result saved in 'result.txt' file.")

    if stop_reached:
        print("Stop action encountered. Stopping the script.")
        exit(0)
