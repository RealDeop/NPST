import os
import math
import time
import random
import string
# Declare global variables
file_found = False
current_directory = os.path.dirname(os.path.abspath(__file__))
directory = os.path.dirname(os.path.abspath(__file__))
prevuse = False
rwscrptf = False
wait = time.sleep
length = 0
count = 0
global set1s
global set2s
global set3s
set1s = False
set2s = True
set3s = True
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))
def generate_random_numbers(count):
    min_value = 0
    max_value = 9
    random_numbers = [random.randint(min_value, max_value) for _ in range(count)]
    return ''.join(map(str, random_numbers))

def values():
    global prevuse, rwscrptf  # Declare global variables
    help_input = input("If you want help, type !help or !commands. If not, press Enter.\n")
    if help_input == "!help":
        print("Facing Issues With The App Contact me at https://github.com/RealDeop/NPST/issues/new\n")
        eots1()
    elif help_input == "!commands":
        print("Here are all the commands and how to use them.\n #10 (or any number you want can be used to copy the line before the # and repeat using the number you put) \n #start (is used to change the start number to anything you want).\n #set (sets the starting number to a specific value).\n #stop (stops the code and saves the changes) \n #end (is the same as #, meaning it adds to the starting number by 1). \n #rest (resets the starting number to 1) ")
        eots1()
    #elif help_input == "!settings":
    #    print("To Change A setting first select a setting number")
    #    set1 = print("| 1 | Quick Shut Down | "+set1s+" |" )
    #    set2 = print("| 2 | Quick Start | "+set2s+" |" )
    #   set3 = print("| 3 | Feedback | "+set3s+" |" )
    #    setnum = input()
    #    if setnum == 1:
    #        print("You Have Choosen setting"+setnum+"it is set To "+set1s+" Change It ? If Yes Type True or False")
    #        tf = input()
    #        set1s = tf
     #   if setnum == 2:
      #      print("You Have Choosen setting"+setnum+"it is set To "+set2s+" Change It ? If Yes Type True or False")
       #     tf2 = input()
        #    set2s = tf2
       # if setnum == 3:
        #    print("You Have Choosen setting"+setsnum+"it is set To "+set3s+" Change It ? If Yes Type True or False")
         #   tf3 = input()
          #  set3s = tf3
            
            
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
            big_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            symbols = '"~`!@#$%^&*()-_=+[]{}\|:;"<,.>/?'
            mulit_letter = True
            strr = ""
            if start_number < 26:
                specified_order = start_number
            if start_number > 25:
                times_over_25 = math.ceil(start_number / 26)  # Calculate how many times it's over 26
                specified_order = start_number - 26 * (times_over_25 - 1)
            while "/str" in line:
                try:
                    str_index = line.find("/str")
                    mulitletter_check = str(line[str_index + 4:].split()[0])
                    strr = str(line[str_index + 4:].split()[0])
                    for letter in letters:
                        if letter.lower() == strr:
                            strr = letter.lower()
                            upper = False
                            line = line.replace("/str " + str(strr), str(letters[(specified_order - 1)]))
                    for letter in symbols:
                            strr = letter.lower()
                            upper = False
                            line = line.replace("/str " + str(strr), str(symbols[(specified_order - 1)]))
                except IndexError:
                    print("Invaild /str Please set a tempory letter and try agian.")
                    break
                except:
                    print("Unkown /str Error Please Contact nspt Github")
                    break
            # Handle /rds command
            while "/rds" in line:
                    rds_index = line.find("/rds")
                    strrr = str(line[rds_index + 5:].split()[0])  # Fixing the index for /rds
                    random_str = generate_random_string(length=int(strrr))
                    line = line.replace(f"/rds {strrr}", str(random_str))
        # Handle /rdi command
            while "/rdi" in line:
                        rdi_index = line.find("/rdi")
                        strri = str(line[rdi_index + 5:].split()[0])  # Fixing the index for /rdi
                        random_int = generate_random_numbers(count=int(strri))
                        line = line.replace(f"/rdi {strri}", str(random_int))
            while "/minus" in line:
                minus_index = line.find("/minus")
                minu = int(line[minus_index + 7:].split()[0])  # Fixing the index for /rdi
                equal = (start_number) - int(minu)
                start_number = equal
                line = line.replace(f"/minus {minu}", str(equal))
            while "/plus" in line:
                plus_index = line.find("/plus")
                plu = int(line[plus_index + 6:].split()[0])  # Fixing the index for /rdi
                equals = (start_number) + int(plu) #startnumber + plu which is the number the user chooses
                start_number = equals
                line = line.replace(f"/plus {plu}", str(equals))
            while "/*" in line:
                muil_index = line.find("/*")
                mui = int(line[muil_index + 3:].split()[0])  # Fixing the index for /rdi
                eequals = (start_number) * int(mui) #startnumber * plu which is the number the user chooses
                start_number = eequals
                line = line.replace(f"/* {mui}", str(eequals))
            while "/d" in line:
                d_index = line.find("/d")
                d = int(line[d_index + 3:].split()[0])  # Fixing the index for /rdi
                eequal = (start_number) / int(d) #startnumber * plu which is the number the user chooses
                start_number = eequal
                line = line.replace(f"/d {d}", str(eequal))
            result += line + "\n"
            start_number += 1

    return result, stop_reached

def main():
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
        eots1()
        if stop_reached:
            print("Stop action encountered. Stopping the script.")
            exit(0)
def eots1():
    print("nspt-terminal tb-0")
    eots = input("Quit ? y | n  User Action:| ") # eots means end of terminal script watiting for user guidince
    if eots.lower() == "y":
        print("program shutting down in \n 3")
        wait(1)
        print("program shutting down in \n 2")
        wait(1)
        print("program shutting down in \n 1")
        wait(1)
        exit(0)
    elif eots.lower() == "n":
        print("program restarting down in \n 1")
        wait(1)
        print("Program starting")
        wait(1)
        main()
    elif eots == "":
        print("program shutting down in \n 1")
        wait(1)
        exit()

    else:
        print("Unkown Input Please Enter in y or n ")
        eots1()
main()
eots1()
