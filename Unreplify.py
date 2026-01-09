import subprocess #Needed for accessing pbcopy and pbpaste

# Lines that start with either of these are considered Python REPL prompts.
PROMPTS = (">>>", "...")

# After a prompt, some sources use a normal space, a tab, or a non-breaking space.
# We remove AT MOST ONE of these characters.
OPTIONAL_AFTER_PROMPT = (" ", "\t", "\u00A0")


def unreplify_main():
    """
    This Function will be the main function
    1 - Access clipboard and store as variable
    2 - Strip The Text of REPL prompts and output a clean formatted string
    3 - Take this new variable and copy it to clipboard
    """
    return

def retrieve_clipboard():
    """Access using pbpaste"""
    return()

def set_clipboard():
    """Set using pbcopy"""
    return()

def clean_string():
    return()