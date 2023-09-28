def help():
    help_input = input("If You Want Help Type !help or !commands if not click enter \n")
    if help_input == "!help":
        print("To Use nspt.py, make a script.txt file and then type anything you want. Replace the number you want to change numerically with 1. To make the script change the number, put a # when you want to change the number and add a one to it. For example: line1 and word 1 # line1 and word 1 \n")
    elif help_input == "!commands":
    	print("Here are all the commands and how to use them.\n #10 (or any number you want can be used to copy the line before the # and repeat using the number you put) \n #start (is used to change the start number to anything you want).\n #stop (stops the code and saves the stuff it changed )\n #end ( is the same as # meaing it adds to the starting number a 1). \n #rest (rests the starting number to 1) ")
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
        else:
            while "1" in line:
                index = line.find("1")
                result += line[:index] + str(start_number)
                line = line[index+1:]

            result += line + "\n"
            start_number += 1

    return result, stop_reached

if __name__ == "__main__":
    help()  # Call the help function

    with open("script.txt", "r") as file:
        script = file.read()

    script_with_hasum = hasum(script)
    replaced_script, stop_reached = replace_numbers(script_with_hasum)

    with open("result.txt", "w") as file:
        file.write(replaced_script)

    print("Result saved in 'result.txt' file.")

    if stop_reached:
        print("Stop action encountered. Stopping the script.")
        exit(0)
