from tkinter import *
from os import system
from platform import system as platform

class noteGui:
    def __init__(self, fname):
        self.fname = fname
        self.root = Tk()
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

    def close(self, evt):
        text = self.scrollTxtArea.getText()
        with open(self.fname, "a") as f:
            f.write(text)
        
        self.root.destroy()
    
    def run(self):
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.attributes("-topmost", False)
        self.root.focus_force()
        self.root.mainloop()

class scrollTxtArea:
    def __init__(self,root):
        frame=Frame(root)
        frame.pack()
        self.textPad(frame)
        return

    def textPad(self,frame):
        #add a frame and put a text area into it
        textPad=Frame(frame)
        self.text=Text(textPad,height=3,width=40)
        
        # add a vertical scroll bar to the text area
        scroll=Scrollbar(textPad)
        self.text.configure(yscrollcommand=scroll.set)
        
        #pack everything
        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT,fill=Y)
        textPad.pack(side=TOP)
        return

    def getText(self):
        return '*' + self.text.get("1.0", END).strip() + '\n'

    def setFocus(self):
        self.text.focus_set()

ng = noteGui("notes.md")
ng.run()
