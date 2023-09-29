import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os

def help_page():
    help_text = "To use this application, create a script and paste on the script diaglog ."
    help_text += "\nFor example: line1 and word 1 # line1 and word 1"
    help_label.config(text=help_text)
    show_page("help")
    return help_text
def commands_page():
    commands_text = "Available commands:\n"
    commands_text += "#10 (or any number) - copy the line before the # and repeat using the number."
    commands_text += "\n#start <number> - change the start number."
    commands_text += "\n#stop or #end - stop the code and save the changes."
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
        else:
            while "1" in line:
                index = line.find("1")
                result += line[:index] + str(start_number)
                line = line[index+1:]

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




