def help():
    help_input = input("If You Want Help Type !help \n")
    if help_input == "!help":
        print("To Use Numeral.py, open the script.txt file and then type anything you want. Replace the number you want to change numerically with 1. To make the script change the number, put a # when you want to change the number and add a one to it. For example: line1 and word 1 # line1 and word 1 \n")
        help()

def hasum(script):
    lines = script.splitlines()
    result = ""

    for line in lines:
        if line.startswith("#"):
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
    line_count = 0
    result = ""

    for line in script.splitlines():
        if line.strip() == "#":
            start_number += 1
        else:
            while "1" in line:
                index = line.find("1")
                result += line[:index] + str(start_number)
                line = line[index+1:]

            result += line + "\n"
            start_number += 1

    return result

if __name__ == "__main__":
    help()  # Call the help function

    with open("script.txt", "r") as file:
        script = file.read()

    script_with_hasum = hasum(script)
    #print("\nScript with Hasum:")
    #print(script_with_hasum)

    replaced_script = replace_numbers(script_with_hasum)
    #print("\nReplaced Script:")
    #print(replaced_script)

    output_file = "result.txt"
    with open(output_file, "w") as file:
        file.write(replaced_script)

    print("Result saved in 'result.txt' file.")

