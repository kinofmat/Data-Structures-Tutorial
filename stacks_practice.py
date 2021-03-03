"""
Kai Matkin

This creates a primitive word processing document. Where you can enter 
a sentance (or more) and can undo one character at a time, or redo one
character at a time. This does not allow for editing the sentance 
further than that. If you'd like a challenge, see if you can make some
changes to the code, that would allow you to choose to edit the
sentance after you have already entered it in.

Remember to read through all of the code that is written so you can 
gain an understanding of what is being done, and what you need to 
change.
"""

doc = [] 
letter_holder = []

"""
This function will take a string passed to it, and initialize the stack 
with each item in the string.
"""
def word_processor(phrase):
    for a in phrase:
        doc.append(a)

"""
This will work as an undo option in the console app. It calls the 
display_phrase function so you can see what changes were made.
"""
def undo():
    #impliment your code here
    
    display_phrase(doc)
    pass

"""
This will work as an redo option (or an undo to your undo) in the console 
app. It calls the display_phrase function so you can see what changes were 
made.
"""
def redo():
    #impliment your code here

    display_phrase(doc)
    pass

"""
The display_phrase function takes a stack as an argument, and then will add 
each item to a string, so that it is more readable for the user. It then 
prints the string for the user to see.
"""
def display_phrase(stack):
    thisstring = ""
    for l in stack:
        thisstring += l
    print(thisstring)

"""
This is what processes the input to create the interface in the console app. 
To allow correction when something is mistyped, it uses recursion. This is 
something that is covered in the unit on Trees. Come back to this code and 
look at it again once you have read about recursion. 
"""
def edit_phrase(command):
    if command == "z" or command == "Z":
        undo()
        return "c"
    elif command == "y" or command == "Y":
        redo()
        return "c"
    elif command == "q" or command == "Q":
        return "q"
    else:
        print("Error! Incorrect value entered.")
        command = input("Press 'z' for undo, 'y' for redo, or 'q' for quit ")
        """
        This function calls itself, which is what makes it recursive. If you 
        aren't careful on how you impliment this, it can very quickly turn 
        into an infinite loop.
        """
        edit_phrase(command)
        return "c"


got_phrase = input("Please enter a sentence ")
word_processor(got_phrase)
print(doc)
q = "c"

"""
As long as the user wants to continue editing the sentance, it will loop to 
allow for more edits
"""
while q == "c":
    command = input("Press z for undo, y for redo, or q for quit ")
    q = edit_phrase(command)