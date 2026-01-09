import subprocess #Needed for accessing pbcopy and pbpaste

# Lines that start with either of these are considered Python REPL prompts.
PROMPTS = (">>>", "...")

# After a prompt, some sources use a normal space, a tab, or a non-breaking space.
# We remove AT MOST ONE of these characters.
OPTIONAL_AFTER_PROMPT = (" ", "\t", "\u00A0")


def unreplify():
    """
    This Function will be the main function
    1 - Access clipboard and store as variable
    2 - Strip The Text of REPL prompts and output a clean formatted string
    3 - Take this new variable and copy it to clipboard
    """
    repl_string = retrieve_clipboard()

    # If Clipboard is empty return 2
    if repl_string.strip() == "":
        return 2
    
    unreplified = unreplify_string(repl_string)

    
    # If stripping did not change anything, don't touch the clipboard.
    if unreplified == repl_string:
        return 1
    
    #Otherwise carry on
    set_clipboard(unreplified)
    return 0

def retrieve_clipboard():
    """Access using pbpaste"""
    return subprocess.check_output(["pbpaste"], text=True)

def set_clipboard(text):
    """Set using pbcopy"""
    subprocess.run(["pbcopy"], input=text, text=True)

def unreplify_string(text):
    lines = text.splitlines() # Need to add \n in after cleaning
    unreplified_lines = []

    for line in lines:
        if line.startswith(PROMPTS):
            line = line[3:] # Removes first 3 charachters

            if line.startswith(OPTIONAL_AFTER_PROMPT):
                line = line[1:] # Removes the tab, space or NBS from new line
        unreplified_lines.append(line)
    
    return "\n".join(unreplified_lines) # Joins the lines back together

# Only run the program when this file is executed directly.
# If the file is imported (for reuse/testing), don't auto-run main() or touch the clipboard.
if __name__ == "__main__":
    raise SystemExit(unreplify())