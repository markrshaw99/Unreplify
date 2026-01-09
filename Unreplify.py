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
    unreplified = unreplify_string(repl_string)
    set_clipboard(unreplified)

    return("Complete")

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
        
    return()