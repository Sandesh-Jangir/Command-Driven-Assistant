# Command-Driven-Assistant
It is a command driven assistant which takes input from the user and give output in selected format (There are 2 Formats one is Standard Output and other is Voice Output) There is a different branch for each format

It uses Python's PyWin32 module to give voice output.

The voice output is given by a function called Speak() which takes string value and speaks it loud.
There is also a mainloop which helps us to take the user's input again and again. If user wants to exit the he has to form the exitcommands list and the program will terminate itself.

There are a list of commands of a specific category of command i.e. BrowserCommands, ExitCommands, etc.
