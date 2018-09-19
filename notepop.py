import tkinter as tk
from os import system
from platform import system as platform

class noteGui:
    def __init__(self, fname):
        self.fname = fname
        self.root = tk.Tk()
        self.scrollTxtArea = scrollTxtArea(self.root)
        self.root.title('Append Note')
        self.root.bind('<Return>', self.close)
        self.root.bind("<FocusIn>", self.handle_focus)

        if platform() == 'Darwin':  # How Mac OS X is identified by Python
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "python" to true' ''')

    def handle_focus(self, evt):
        if evt.widget == self.root:
            self.root.focus_set()
            self.scrollTxtArea.setFocus()

    def close(self, evt=None):
        text = self.scrollTxtArea.getText()
        self.root.destroy()
        with open(self.fname, "a") as f:
            f.write(text)
    
    def run(self):
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.attributes("-topmost", False)
        self.root.focus_force()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.mainloop()

class scrollTxtArea:
    def __init__(self,root):
        frame=tk.Frame(root)
        frame.pack()
        self.textPad(frame)
        return

    def textPad(self,frame):
        #add a frame and put a text area into it
        textPad=tk.Frame(frame)
        self.text=tk.Text(textPad,height=3,width=40)
        
        # add a vertical scroll bar to the text area
        scroll=tk.Scrollbar(textPad)
        self.text.configure(yscrollcommand=scroll.set)
        
        #pack everything
        self.text.pack(side=tk.LEFT)
        scroll.pack(side=tk.RIGHT,fill=tk.Y)
        textPad.pack(side=tk.TOP)
        return

    def getText(self):
        text = self.text.get("1.0", tk.END).strip() 
        if text != "":
            return '* ' + text + '\n'

    def setFocus(self):
        self.text.focus_set()

if __name__ == '__main__':
    ng = noteGui("/Users/thomas/Dropbox/PhD/notes.md")
    ng.run()
