notepop
===

You're working on a project and trying to take notes. 

Everytime you take notes, you have to switch applications. You lose context.

Use `notepop` instead. Open a note with a shortcut. Type in your note without losing your context, and then close it.

`notepop` is lightweight. Notes get appended to a text file for you to review later. 

Automator shortcut: ctrl+option+cmd+n

ctrl+tab to focus to category pane, tab to focus back to textarea.

# Development setup (Mac)
1. Clone the repo
2. Update the config file and global variables with your paths
3. Set up an Automator Service to run a bash script that runs `notepop.sh`.
4. Set up a shortcut that calls the Automator Service.