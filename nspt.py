import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import math

def help_page():
    help_text = "To use this application, create a script and paste on the script diaglog ."
    help_text += "\nFor example: line/int 1 and word/int 1 \n#\n line/int 1 and word/int 1"
    help_label.config(text=help_text)
    show_page("help")
    return help_text
def commands_page():
    commands_text = "Available commands:\n"
    commands_text = "# or #end - Change the specfied by one \n"
    commands_text += "#10 (or any number) - copy the line before the # and repeat using the number."
    commands_text += "\n#start or #set - <number> - change the start number."
    commands_text += "\n#stop - stop the code and save the changes."
    commands_text += "\n#rest - reset the starting number to 1."
    commands_label.config(text=commands_text)
    show_page("commands")
    return commands_text

def show_page(page_name):
    for page, label in pages.items():
        if page == page_name:
            label.pack()
        else:
            label.pack_forget()


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
    pass

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
    pass

def run_application():
    script = script_entry.get("1.0", tk.END)

    script_with_hasum = hasum(script)
    replaced_script, stop_reached = replace_numbers(script_with_hasum)

    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, replaced_script)
    result_text.config(state=tk.DISABLED)

    result_saved_text = f"Result saved in 'result.txt' file."

    if stop_reached:
        stop_text = "Stop action encountered. Stopping the script."
    else:
        stop_text = ""

    print(result_saved_text)
    print(stop_text)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Numeral GUI")
    root.geometry("700x500")
    # Create a frame to hold the pages
    page_frame = ttk.Frame(root)
    page_frame.pack(fill="both", expand=True)

    # Script entry
    script_label = ttk.Label(page_frame, text="Script:")
    script_label.pack()
    script_entry = tk.Text(page_frame, height=5, width=50)
    script_entry.pack()

    # Run button
    run_button = ttk.Button(page_frame, text="Run Application", command=run_application)
    run_button.pack(pady=10)

    # Result display
    result_label = ttk.Label(page_frame, text="Result:")
    result_label.pack()
    result_text = tk.Text(page_frame, height=10, width=50)
    result_text.pack()
    result_text.config(state=tk.DISABLED)

    # Help page
    help_label = ttk.Label(page_frame, text="")
    help_button = ttk.Button(page_frame, text="Help", command=help_page)
    help_button.pack(pady=10)

    # Commands page
    commands_label = ttk.Label(page_frame, text="")
    commands_button = ttk.Button(page_frame, text="Commands", command=commands_page)
    commands_button.pack(pady=10, padx=10)

    # Define pages
    pages = {"help": help_label, "commands": commands_label}
    
    root.mainloop()




