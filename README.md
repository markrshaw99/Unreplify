# unreplify

<p align="center">
	<img src="unreplifyLogo.png" alt="unreplify logo" width="300" />
</p>

unreplify is a small macOS utility that removes Python REPL prompts (`>>>` and `...`) from copied code, so it can be pasted directly into `.py` files without manual editing.

It strips prompts only when they appear at the **start of a line**, and it also removes **one optional separator character** after the prompt (space, tab, or a non-breaking space).

It’s designed to be triggered via a **global keyboard shortcut** using a macOS **Quick Action (Automator)** and provides clear audio + visual feedback.

---

## Setup video

![Setup demo](docs/unreplify_setup.gif)

## The problem it solves

Many Python tutorials, documentation pages, and books present examples in REPL format, such as:

```text
>>> class Greeter():
...     def __init__(self, name):
...         self.name = name
...
...     def hello(self):
...         return f"Hello, {self.name}"
...
>>> greeter = Greeter("Alan")
>>> greeter.hello()
```

Pasting this directly into a `.py` file results in syntax errors.

unreplify automatically removes the REPL prompts so the result becomes valid Python source code:

```python
class Greeter():
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f"Hello, {self.name}"

greeter = Greeter("Alan")
greeter.hello()
```

---

## Features

* Removes `>>>` and `...` Python REPL prompts
* Also removes one optional character after the prompt (` `, tab, or non-breaking space)
* Preserves indentation exactly
* Three distinct outcomes with clear feedback:

	* Clipboard cleaned
	* No REPL prompts found
	* Clipboard empty
* Different system sounds for each outcome
* 1-second auto-dismissing pop-up confirmation
* No visible Terminal windows
* No third-party Python dependencies
* Fully macOS-native (Automator + AppleScript)

---

## Requirements

* macOS
* Python 3 (the system Python installation is sufficient)

---

## Installation

### 1. Get `unreplify.py`

Download this repository (or clone it), then place `unreplify.py` somewhere permanent, for example:

```text
~/Scripts/unreplify/unreplify.py
```

You may choose any location, but if you move the file later you must update the path in Automator.

---

### 2. Create a Quick Action (Automator)

1. Open **Automator**
2. Click **New Document**
3. Choose **Quick Action**

At the top of the workflow, set:

* **Workflow receives current:** `no input`
* **in:** `any application`

---

### 3. Add “Run Shell Script”

1. Add the **Run Shell Script** action
2. Configure it as follows:

	 * **Shell:** `/bin/zsh`
	 * **Pass input:** `to stdin`

Paste the following code, replacing **`/full/path/to/unreplify.py`** with the location of your `unreplify.py` file:


```bash
/usr/bin/python3 "/full/path/to/unreplify.py"
rc=$?

if [ "$rc" -eq 0 ]; then
	sound="/System/Library/Sounds/Glass.aiff"
	msg="Clipboard cleaned"
elif [ "$rc" -eq 1 ]; then
	sound="/System/Library/Sounds/Pop.aiff"
	msg="No REPL prompts found"
else
	sound="/System/Library/Sounds/Submarine.aiff"
	msg="Clipboard is empty"
fi

afplay "$sound" >/dev/null 2>&1 &
/usr/bin/osascript <<APPLESCRIPT
display dialog "$msg" with title "unreplify" giving up after 1
APPLESCRIPT
```

---

### 4. Save the Quick Action

* Select **File → Save**
* Name it **unreplify**

---

## Assign a Keyboard Shortcut

1. Open **System Settings**
2. Go to **Keyboard → Keyboard Shortcuts**
3. Select **Services**
4. Locate **unreplify** (typically under **General**)
5. Assign a shortcut, for example:

```text
Ctrl + Option + Command + V
```

This combination is unlikely to conflict with existing system shortcuts.

---

## Usage

1. Copy Python REPL code containing `>>>` and/or `...`
2. Press your unreplify keyboard shortcut
3. Hear a sound and see a brief confirmation pop-up
4. Paste clean Python code into your editor

---

## Notes

* unreplify only strips prompts at the start of a line (it won’t touch `>>>` inside strings or mid-line).
* Each user must create the Quick Action locally.
* Automator workflows are not portable between machines.
* Only `unreplify.py` is shared; all macOS wiring is user-specific.
* The script is safe to run repeatedly.

---

## Exit codes

When run directly (for example via Automator), `unreplify.py` exits with:

* `0` — clipboard cleaned (prompts removed and clipboard updated)
* `1` — no REPL prompts found (clipboard left unchanged)
* `2` — clipboard empty/whitespace (clipboard left unchanged)

---

## License

MIT
