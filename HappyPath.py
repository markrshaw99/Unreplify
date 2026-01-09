"""

Goal - Build a tiny macOS utility that takes Python code copied from the Makers Journey that is in
REPL form (lines starting with ">>>" or "...") and turns it into normal Python
source that can be pasted into VS Code (.py files) without syntax errors.

What “success” looks like
-------------------------
1) Copy something like this:

    >>> class Person:
    ...     def __init__(self, name):
    ...         self.name = name

2) Run this program through some kind of keyboard shortcut.

3) Clipboard now contains:

    class Person:
        def __init__(self, name):
            self.name = name

Happy Path
----------
A) Only strip prompts when they appear at the START of a line.
   - We do NOT remove ">>>" if it appears later in the line (inside a string,
     comment, or in the middle of text).

B) Prompts to strip:
   - ">>>": the primary Python REPL prompt
   - "...": the continuation prompt

C) After the prompt, optionally remove ONE separator character.
   - Many sources format as: ">>> " (prompt + space)
   - Some sources copy with: tab or non-breaking space
   - Remove at most one of: space, tab, NBSP

D) Preserve everything else:
   - Keep indentation after the prompt removal (that’s the point)
   - Keep blank lines (as they appear after processing)

Plan
-----
Step 1: A pure function that transforms text:
    strip_repl_prompts(text) -> cleaned_text

    Approach:
    - Split the input into lines: text.splitlines()
      (Note: splitlines() removes newline characters; when we join with '\n',
       output newlines become normalized. This is acceptable for our use-case.)
    - For each line:
        - If it starts with ">>>" or "...":
            - Remove the first 3 characters
            - If the next character is one optional separator (space/tab/NBSP),
              remove that single character too
        - Append the result to cleaned_lines
    - Return "\n".join(cleaned_lines)

Step 2: Clipboard integration (macOS-only):
    - Read clipboard by running: pbpaste
    - Write clipboard by running: pbcopy (send text to stdin)

Step 3: main() and exit codes:
    - Read clipboard into `original`
    - If original is empty or only whitespace -> return 2
    - Clean it
    - If cleaned is identical -> return 1 (do not modify clipboard)
    - Else write cleaned back to clipboard -> return 0

This allows:
- Running directly: python3 FixPaste.py
- Importing safely (no clipboard side effects on import)

"""